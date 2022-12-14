import json
from utils.meta_wrapper import JSR
from django.views import View
from forum.models import Question, Content, Tag
from user.models import User
from datetime import datetime


class ForumList(View):
    @JSR('status', 'total', 'list')
    def get(self, request):
        if dict(request.GET).keys() != {'page', 'each', 'filter'}:
            return 1, 0, []
        try:
            page = int(request.GET.get('page'))
            each = int(request.GET.get('each'))
            tag = request.GET.get('filter')
        except ValueError:
            return 1, 0, []

        all_question = []
        try:
            if tag == 'all':
                all_question_set = Question.objects.all()
                for q in all_question_set:
                    all_question.append(q)
            elif tag == 'expert':
                all_question_set = Question.objects.filter(expert_reply__exact=True)
                for q in all_question_set:
                    all_question.append(q)
            else:
                all_tagged_question = Tag.objects.filter(name__exact=tag)
                for q in all_tagged_question:
                    if q.question not in all_question:
                        all_question.append(q.question)
        except:
            return 7, 0, []

        total = len(all_question)
        question_list = []
        all_question.sort(key=lambda x: x.published_time, reverse=True)
        for question in all_question[(page - 1) * each: page * each]:
            publish_user = question.user
            user = {
                'name': publish_user.name,
                'avatar': publish_user.avatar,
                'uid': str(publish_user.id),
                'is_expert': publish_user.identity == 2
            }
            question_list.append({
                'user': user,
                'title': question.title,
                'preview': question.question_all_content.order_by('published_time').first().content[:300],
                'views': question.views,
                'published_time': question.published_time,
                'replied_time': question.replied_time if question.replied_time else '',
                'expert_reply': question.expert_reply,
                'solved': question.solved,
                'qid': str(question.id)
            })

        return 0, total, question_list


class ForumQuestion(View):
    @JSR('status', 'uid', 'solved', 'total', 'title', 'published_time', 'views', 'list', 'tag')
    def get(self, request):
        if dict(request.GET).keys() != {'qid', 'page', 'each'}:
            return 1, 0, '', '', 0, []
        try:
            qid = int(request.GET.get('qid'))
            page = int(request.GET.get('page'))
            each = int(request.GET.get('each'))
        except ValueError:
            return 1, 0, '', '', 0, []
        try:
            question = Question.objects.get(id=qid)
        except:
            return 2, 0, '', '', 0, []
        all_content = question.question_all_content.all().order_by('-is_top', 'published_time')
        total = all_content.count()
        title = question.title
        published_time = question.published_time
        views = question.views
        content_list = []
        for index in range((page - 1) * each, min(total, page*each)):
            content = all_content[index]
            if content.replied_content is None:
                floor = -1
            else:
                floor = content.replied_content.floor
            publish_user = content.user
            user = {
                'name': publish_user.name,
                'avatar': publish_user.avatar,
                'uid': str(publish_user.id),
                'is_expert': publish_user.identity == 2
            }
            content_list.append({
                'user': user,
                'content': content.content,
                'is_top': content.is_top,
                'rid': str(content.id),
                'floor': content.floor,
                'replied_floor': floor,
                'reply': {'name': content.replied_content.user.name if content.replied_content else '', 'uid': str(content.replied_content.user_id) if content.replied_content else ''},
                'published_time': content.published_time
            })
        tags = Tag.objects.filter(question=question)
        tag = []
        for t in tags:
            tag.append(t.name)
        return 0, str(question.user_id), question.solved, total, title, published_time, views, content_list, tag


class ForumPublish(View):
    @JSR('status', 'qid')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403, ''
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1, ''
        u = u.get()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'title', 'content', 'tags'}:
            return 1, ''
        print('111')
        question = Question.objects.create(title=kwargs['title'], user=u, published_time=now)
        print('222')
        content_num = question.question_all_content.count()
        Content.objects.create(question=question, user=u, published_time=now, content=kwargs['content'], floor=content_num + 1)
        for tag in kwargs['tags']:
            Tag.objects.create(name=tag, question=question)
        return 0, str(question.id)


class ForumReply(View):
    @JSR('status', 'rid', 'replied_time')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403, 0, ''
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1, 0, ''
        u = u.get()
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'qid', 'rid', 'content'}:
            return 1, 0, ''
        try:
            if kwargs['qid'] == '':
                question = Content.objects.get(id=kwargs['rid']).question
            else:
                question = Question.objects.get(id=kwargs['qid'])
        except:
            return 2, 0, ''
        question.replied_time = now
        question.save()
        content_num = question.question_all_content.count()
        content = Content.objects.create(content=kwargs['content'], user=u, published_time=now, question=question, floor=content_num+1)
        if kwargs['rid'] != '':
            content.replied_content_id = int(kwargs['rid'])
        if content.user.identity == 2:
            content.question.expert_reply = True
            if Tag.objects.filter(question=content.question, name='expert').count() == 0:
                Tag.objects.create(question=content.question, name='expert')
        content.save()
        content.question.save()
        return 0, str(content.id), now


class ForumEdit(View):
    @JSR('status')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1
        u = u.get()
        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'qid', 'rid', 'content'}:
            return 1
        if kwargs['qid'] == '':
            content = Content.objects.get(id=kwargs['rid'])
            if content.user != u:
                return 2
            content.content = kwargs['content']
            content.save()
        else:
            question = Question.objects.get(id=kwargs['qid'])
            if question.user != u:
                return 2
            question.title = kwargs['content']
            question.save()
        return 0


class ForumDelete(View):
    @JSR('status')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1
        u = u.get()
        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'qid', 'rid'}:
            return 1
        if kwargs['qid'] == '':
            content = Content.objects.get(id=kwargs['rid'])
            question = content.question
            if content.user != u:
                return 2
            content.delete()
            contents = question.question_all_content.all().order_by('published_time')
            for index in range(contents.count()):
                contents[index].floor = index + 1
                contents[index].save()
        else:
            question = Question.objects.get(id=kwargs['qid'])
            if question.user != u:
                return 2
            question.delete()
        return 0


class ForumSolve(View):
    @JSR('status', 'solved')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403, False
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1, False
        u = u.get()
        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'qid'}:
            return 1, False
        try:
            question = Question.objects.get(id=int(kwargs['qid']))
        except:
            return 2, False
        if question.user != u:
            return 3, False
        question.solved = not question.solved
        question.save()
        return 0, question.solved


class ForumTop(View):
    @JSR('status', 'is_top')
    def post(self, request):
        if not request.session.get('is_login', False):
            return 403, False
        try:
            u = User.objects.filter(id=request.session['uid'])
        except:
            uid = request.session['uid'].decode() if isinstance(request.session['uid'], bytes) else request.session[
                'uid']
            u = User.objects.filter(id=int(uid))
        if not u.exists():
            return -1, False
        u = u.get()


        kwargs: dict = json.loads(request.body)
        if kwargs.keys() != {'rid'}:
            return 1, False
        try:
            content = Content.objects.get(id=int(kwargs['rid']))
        except:
            return 2, False
        if u.identity == 1 and content.user != u:
            return 403, False
        content.is_top = not content.is_top
        content.save()
        return 0, content.is_top
