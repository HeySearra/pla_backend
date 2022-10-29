import json

country_str =  '{"country": ["\u4e2d\u56fd", "\u963f\u5c14\u5df4\u5c3c\u4e9a", "\u963f\u5c14\u53ca\u5229\u4e9a", ' \
               '"\u963f\u5bcc\u6c57", "\u963f\u6839\u5ef7", "\u963f\u62c9\u4f2f\u8054\u5408\u914b\u957f\u56fd", ' \
               '"\u963f\u9c81\u5df4", "\u963f\u66fc", "\u963f\u585e\u62dc\u7586", "\u963f\u68ee\u677e\u5c9b", ' \
               '"\u57c3\u53ca", "\u57c3\u585e\u4fc4\u6bd4\u4e9a", "\u7231\u5c14\u5170", "\u7231\u6c99\u5c3c\u4e9a", ' \
               '"\u5b89\u9053\u5c14", "\u5b89\u54e5\u62c9", "\u5b89\u572d\u62c9", ' \
               '"\u5b89\u63d0\u74dc\u5c9b\u548c\u5df4\u5e03\u8fbe", "\u6fb3\u5927\u5229\u4e9a", "\u5965\u5730\u5229", ' \
               '"\u5965\u5170\u7fa4\u5c9b", "\u5df4\u5df4\u591a\u65af\u5c9b", ' \
               '"\u5df4\u5e03\u4e9a\u65b0\u51e0\u5185\u4e9a", "\u5df4\u54c8\u9a6c", "\u5df4\u57fa\u65af\u5766", ' \
               '"\u5df4\u62c9\u572d", "\u5df4\u52d2\u65af\u5766", "\u5df4\u6797", "\u5df4\u62ff\u9a6c", ' \
               '"\u5df4\u897f", "\u767d\u4fc4\u7f57\u65af", "\u767e\u6155\u5927", "\u4fdd\u52a0\u5229\u4e9a", ' \
               '"\u5317\u9a6c\u91cc\u4e9a\u7eb3\u7fa4\u5c9b", "\u8d1d\u5b81", "\u6bd4\u5229\u65f6", "\u51b0\u5c9b", ' \
               '"\u6ce2\u591a\u9ece\u5404", "\u6ce2\u5170", "\u73bb\u5229\u7ef4\u4e9a", ' \
               '"\u6ce2\u65af\u5c3c\u4e9a\u548c\u9ed1\u585e\u54e5\u7ef4\u90a3", "\u535a\u8328\u74e6\u7eb3", ' \
               '"\u4f2f\u5229\u5179", "\u4e0d\u4e39", "\u5e03\u57fa\u7eb3\u6cd5\u7d22", "\u5e03\u9686\u8fea", ' \
               '"\u5e03\u97e6\u5c9b", "\u671d\u9c9c", "\u4e39\u9ea6", "\u5fb7\u56fd", "\u4e1c\u5e1d\u6c76", ' \
               '"\u591a\u54e5", "\u591a\u7c73\u5c3c\u52a0", "\u591a\u7c73\u5c3c\u52a0\u5171\u548c\u56fd", ' \
               '"\u4fc4\u7f57\u65af", "\u5384\u74dc\u591a\u5c14", "\u5384\u7acb\u7279\u91cc\u4e9a", "\u6cd5\u56fd", ' \
               '"\u6cd5\u7f57\u7fa4\u5c9b", "\u6cd5\u5c5e\u6ce2\u5229\u5c3c\u897f\u4e9a", ' \
               '"\u6cd5\u5c5e\u572d\u4e9a\u90a3", "\u6cd5\u5c5e\u5357\u90e8\u9886\u5730", "\u68b5\u8482\u5188", ' \
               '"\u83f2\u5f8b\u5bbe", "\u6590\u6d4e", "\u82ac\u5170", "\u4f5b\u5f97\u89d2", ' \
               '"\u5f17\u5170\u514b\u7fa4\u5c9b", "\u5188\u6bd4\u4e9a", "\u521a\u679c", ' \
               '"\u521a\u679c\u6c11\u4e3b\u5171\u548c\u56fd", "\u54e5\u4f26\u6bd4\u4e9a", ' \
               '"\u54e5\u65af\u8fbe\u9ece\u52a0", "\u683c\u6069\u897f\u5c9b", "\u683c\u6797\u7eb3\u8fbe", ' \
               '"\u683c\u9675\u5170", "\u53e4\u5df4", "\u74dc\u5fb7\u7f57\u666e", "\u5173\u5c9b", ' \
               '"\u572d\u4e9a\u90a3", "\u54c8\u8428\u514b\u65af\u5766", "\u6d77\u5730", "\u97e9\u56fd", ' \
               '"\u8377\u5170", "\u8377\u5c5e\u5b89\u5730\u5217\u65af", ' \
               '"\u8d6b\u5fb7\u548c\u9ea6\u514b\u5510\u7eb3\u7fa4\u5c9b", "\u6d2a\u90fd\u62c9\u65af", ' \
               '"\u57fa\u91cc\u5df4\u65af", "\u5409\u5e03\u63d0", "\u5409\u5c14\u5409\u65af\u65af\u5766", ' \
               '"\u51e0\u5185\u4e9a", "\u51e0\u5185\u4e9a\u6bd4\u7ecd", "\u52a0\u62ff\u5927", "\u52a0\u7eb3", ' \
               '"\u52a0\u84ec", "\u67ec\u57d4\u5be8", "\u6377\u514b\u5171\u548c\u56fd", "\u6d25\u5df4\u5e03\u97e6", ' \
               '"\u5580\u9ea6\u9686", "\u5361\u5854\u5c14", "\u5f00\u66fc\u7fa4\u5c9b", ' \
               '"\u79d1\u79d1\u65af\u7fa4\u5c9b", "\u79d1\u6469\u7f57", "\u79d1\u7279\u8fea\u74e6", ' \
               '"\u79d1\u5a01\u7279", "\u514b\u7f57\u5730\u4e9a", "\u80af\u5c3c\u4e9a", "\u5e93\u514b\u7fa4\u5c9b", ' \
               '"\u62c9\u8131\u7ef4\u4e9a", "\u83b1\u7d22\u6258", "\u8001\u631d", "\u9ece\u5df4\u5ae9", ' \
               '"\u5229\u6bd4\u91cc\u4e9a", "\u5229\u6bd4\u4e9a", "\u7acb\u9676\u5b9b", ' \
               '"\u5217\u652f\u6566\u58eb\u767b", "\u7559\u5c3c\u65fa\u5c9b", "\u5362\u68ee\u5821", ' \
               '"\u5362\u65fa\u8fbe", "\u7f57\u9a6c\u5c3c\u4e9a", "\u9a6c\u8fbe\u52a0\u65af\u52a0", ' \
               '"\u9a6c\u5c14\u4ee3\u592b", "\u9a6c\u8033\u4ed6", "\u9a6c\u62c9\u7ef4", "\u9a6c\u6765\u897f\u4e9a", ' \
               '"\u9a6c\u91cc", "\u9a6c\u5176\u987f", "\u9a6c\u7ecd\u5c14\u7fa4\u5c9b", "\u9a6c\u63d0\u5c3c\u514b", ' \
               '"\u9a6c\u7ea6\u7279\u5c9b", "\u66fc\u5c9b", "\u6bdb\u91cc\u6c42\u65af", ' \
               '"\u6bdb\u91cc\u5854\u5c3c\u4e9a", "\u7f8e\u56fd", "\u7f8e\u5c5e\u8428\u6469\u4e9a", ' \
               '"\u7f8e\u5c5e\u5916\u5c9b", "\u8499\u53e4", "\u8499\u7279\u585e\u62c9\u7279", "\u5b5f\u52a0\u62c9", ' \
               '"\u5bc6\u514b\u7f57\u5c3c\u897f\u4e9a", "\u79d8\u9c81", "\u7f05\u7538", "\u6469\u5c14\u591a\u74e6", ' \
               '"\u6469\u6d1b\u54e5", "\u6469\u7eb3\u54e5", "\u83ab\u6851\u6bd4\u514b", "\u58a8\u897f\u54e5", ' \
               '"\u7eb3\u7c73\u6bd4\u4e9a", "\u5357\u975e", "\u5357\u6781\u6d32", ' \
               '"\u5357\u4e54\u6cbb\u4e9a\u548c\u5357\u6851\u5fb7\u5a01\u5947\u7fa4\u5c9b", "\u7459\u9c81", ' \
               '"\u5c3c\u6cca\u5c14", "\u5c3c\u52a0\u62c9\u74dc", "\u5c3c\u65e5\u5c14", "\u5c3c\u65e5\u5229\u4e9a", ' \
               '"\u7ebd\u57c3", "\u632a\u5a01", "\u8bfa\u798f\u514b", "\u5e15\u52b3\u7fa4\u5c9b", ' \
               '"\u76ae\u7279\u51ef\u6069", "\u8461\u8404\u7259", "\u4e54\u6cbb\u4e9a", "\u65e5\u672c", ' \
               '"\u745e\u5178", "\u745e\u58eb", "\u8428\u5c14\u74e6\u591a", "\u8428\u6469\u4e9a", ' \
               '"\u585e\u5c14\u7ef4\u4e9a,\u9ed1\u5c71", "\u585e\u62c9\u5229\u6602", "\u585e\u5185\u52a0\u5c14", ' \
               '"\u585e\u6d66\u8def\u65af", "\u585e\u820c\u5c14", "\u6c99\u7279\u963f\u62c9\u4f2f", ' \
               '"\u5723\u8bde\u5c9b", "\u5723\u591a\u7f8e\u548c\u666e\u6797\u897f\u6bd4", "\u5723\u8d6b\u52d2\u62ff", ' \
               '"\u5723\u57fa\u8328\u548c\u5c3c\u7ef4\u65af", "\u5723\u5362\u897f\u4e9a", "\u5723\u9a6c\u529b\u8bfa", ' \
               '"\u5723\u76ae\u57c3\u5c14\u548c\u7c73\u514b\u9686\u7fa4\u5c9b", ' \
               '"\u5723\u6587\u68ee\u7279\u548c\u683c\u6797\u7eb3\u4e01\u65af", "\u65af\u91cc\u5170\u5361", ' \
               '"\u65af\u6d1b\u4f10\u514b", "\u65af\u6d1b\u6587\u5c3c\u4e9a", ' \
               '"\u65af\u74e6\u5c14\u5df4\u548c\u626c\u9a6c\u5ef7", "\u65af\u5a01\u58eb\u5170", "\u82cf\u4e39", ' \
               '"\u82cf\u91cc\u5357", "\u6240\u7f57\u95e8\u7fa4\u5c9b", "\u7d22\u9a6c\u91cc", ' \
               '"\u5854\u5409\u514b\u65af\u5766", "\u6cf0\u56fd", "\u5766\u6851\u5c3c\u4e9a", "\u6c64\u52a0", ' \
               '"\u7279\u514b\u65af\u548c\u51ef\u514b\u7279\u65af\u7fa4\u5c9b", ' \
               '"\u7279\u91cc\u65af\u5766\u8fbe\u6606\u54c8", "\u7279\u7acb\u5c3c\u8fbe\u548c\u591a\u5df4\u54e5", ' \
               '"\u7a81\u5c3c\u65af", "\u56fe\u74e6\u5362", "\u571f\u8033\u5176", "\u571f\u5e93\u66fc\u65af\u5766", ' \
               '"\u6258\u514b\u52b3", "\u74e6\u5229\u65af\u548c\u798f\u56fe\u7eb3", "\u74e6\u52aa\u963f\u56fe", ' \
               '"\u5371\u5730\u9a6c\u62c9", "\u7ef4\u5c14\u4eac\u7fa4\u5c9b\uff0c\u7f8e\u5c5e", ' \
               '"\u7ef4\u5c14\u4eac\u7fa4\u5c9b\uff0c\u82f1\u5c5e", "\u59d4\u5185\u745e\u62c9", "\u6587\u83b1", ' \
               '"\u4e4c\u5e72\u8fbe", "\u4e4c\u514b\u5170", "\u4e4c\u62c9\u572d", ' \
               '"\u4e4c\u5179\u522b\u514b\u65af\u5766", "\u897f\u73ed\u7259", "\u5e0c\u814a", "\u65b0\u52a0\u5761", ' \
               '"\u65b0\u5580\u91cc\u591a\u5c3c\u4e9a", "\u65b0\u897f\u5170", "\u5308\u7259\u5229", ' \
               '"\u53d9\u5229\u4e9a", "\u7259\u4e70\u52a0", "\u4e9a\u7f8e\u5c3c\u4e9a", "\u4e5f\u95e8", ' \
               '"\u4f0a\u62c9\u514b", "\u4f0a\u6717", "\u4ee5\u8272\u5217", "\u610f\u5927\u5229", "\u5370\u5ea6", ' \
               '"\u5370\u5ea6\u5c3c\u897f\u4e9a", "\u82f1\u56fd", "\u82f1\u5c5e\u5370\u5ea6\u6d0b\u9886\u5730", ' \
               '"\u7ea6\u65e6", "\u8d8a\u5357", "\u8d5e\u6bd4\u4e9a", "\u6cfd\u897f\u5c9b", "\u4e4d\u5f97", ' \
               '"\u76f4\u5e03\u7f57\u9640", "\u667a\u5229", "\u4e2d\u975e\u5171\u548c\u56fd"]} '


def get_country_ch_list():
    return json.loads(country_str)['country']


if __name__ == '__main__':
    print(get_country_ch_list())
