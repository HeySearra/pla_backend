import json
import os
from meta_config import SPIDER_DATA_DIRNAME
import datetime


# date -> str: 2021-07-09
def epidemic_China_total_import(date: str):
    China_data = {
        "new": {
            "died": 0,
            "cured": 0,
            "confirmed": 0,
            "vaccinated": "未知",
        },
        'total': {
            'died': 0,
            'cured': 0,
            'confirmed': 0,
            "vaccinated": "未知",
        },
    }
    provinces_json = os.path.join(SPIDER_DATA_DIRNAME, 'epidemic_domestic_data', 'province.json')
    provinces = json.load(open(provinces_json, 'r', encoding='utf-8'))
    data = None
    for it in provinces:
        if it['date'] == date:
            data = it
    if not data:
        return None  # shit
    for it in data['provinces']:
        China_data['total']['died'] += it['total']['died']
        China_data['total']['cured'] += it['total']['cured']
        China_data['total']['confirmed'] += it['total']['confirmed']
        China_data['new']['died'] += it['new']['died']
        China_data['new']['cured'] += it['new']['cured']
        China_data['new']['confirmed'] += it['new']['confirmed']

    return China_data


cached_china_total = None


def epidemic_china_total_alldate_import():
    global cached_china_total
    if cached_china_total is None:
        cached_china_total = []
        nowdate = datetime.date(2020, 1, 28)
        while nowdate != datetime.date(2021, 7, 11):
            res = epidemic_China_total_import(nowdate.isoformat()) or {}
            res['date'] = nowdate.isoformat()
            cached_china_total.append(res)
    return cached_china_total
