import json
from datetime import datetime, timedelta

from django.views import View

from news.models import News, Rumor, NewsPolicy
from utils.meta_wrapper import JSR


class WeeklyNews(View):
    OVERSEA_KEYS = {
        '世界卫生', '世卫', '全球', '驻美',
        '东南亚', '日本', '日方', '东京', '韩', '首尔', '朝鲜', '泰', '老挝', '缅甸', '柬埔寨', '越南',
        '印度', '印尼', '新加坡', '马来西亚', '印度尼西亚', '东盟', '南非',
        '英格兰', '英国', '伦敦', '法国', '巴黎', '戛纳', '德国', '意大利', '秘鲁', '葡萄牙',
        '瑞士', '希腊', '比利时', '以色列', '土耳其', '阿富汗', '阿拉伯',
        '美国', '全美', '北美', '澳',
        '智利', '巴西', '南美',
        '俄罗斯', '伊拉克',
    }

    @JSR('status', 'date', 'china', 'global')
    def post(self, request):
        # new_news = news_spider()
        kwargs: dict = json.loads(request.body)
        res_china, res_global = [], []
        today_date = datetime.now().date()

        if kwargs.get('date') is None or kwargs['date'] == '':
            WeeklyNews.res_append(News.objects.all(), res_china, res_global)
        else:
            try:
                someday_date = datetime.strptime(kwargs['date'].split('T')[0], '%Y-%m-%d').date()
                WeeklyNews.res_append(News.objects.filter(publish_time=someday_date), res_china, res_global)
            except:
                return 2, '', [], []

        return 0, today_date.strftime('%Y-%m-%d'), res_china, res_global

    @staticmethod
    def res_append(query, res_china, res_global):
        for a in query:
            a: News
            china, title = True, a.title
            for oversea_key in WeeklyNews.OVERSEA_KEYS:
                if oversea_key in title:
                    china = False
                    break
            (res_china if china else res_global).append({
                'title': a.title,
                'body': a.context,
                'url': a.url,
                'publish_time': a.publish_time.strftime('%Y-%m-%d'),
                'media_name': a.media,
                'img_url': a.img if a.img else '',
            })


class PolicyNews(View):
    @JSR('status', 'date', 'china', 'global')
    def post(self, request):
        # new_news = news_spider()
        kwargs: dict = json.loads(request.body)
        res_china, res_global = [], []
        today_date = datetime.now().date()

        if kwargs.get('date') is None or kwargs['date'] == '':
            PolicyNews.res_append(NewsPolicy.objects.all(), res_china, res_global)
        else:
            try:
                someday_date = datetime.strptime(kwargs['date'].split('T')[0], '%Y-%m-%d').date()
                PolicyNews.res_append(NewsPolicy.objects.filter(publish_time=someday_date), res_china, res_global)
            except:
                return 2, '', [], []

        return 0, today_date.strftime('%Y-%m-%d'), res_china, res_global

    @staticmethod
    def res_append(query, res_china, res_global):
        for a in query:
            a: News
            china, title = True, a.title
            for oversea_key in WeeklyNews.OVERSEA_KEYS:
                if oversea_key in title:
                    china = False
                    break
            (res_china if china else res_global).append({
                'title': a.title,
                'url': a.url,
                'publish_time': a.publish_time.strftime('%Y-%m-%d'),
                'media_name': a.media,
            })


class RumorList(View):
    @JSR('status', 'data')
    def post(self, request):
        res = []
        for a in Rumor.objects.all():
            res.append({
                'title': a.title,
                'summary': a.summary,
                'body': a.body,
            })
        return 0, res
