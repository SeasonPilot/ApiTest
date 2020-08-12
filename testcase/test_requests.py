# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/11 20:32
# 文件名：test_requests.py
# 开发工具：PyCharm
import logging
import requests
import json
import pytest


class TestRequests:
    logging.basicConfig(level=logging.INFO)

    def test_xuqiu(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=2')
        logging.info(r)
        logging.info(json.dumps(r.json(), indent=2))

    def test_xueqiu_quote(self):
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json'
        # 这样写是错误的
        # params = {
        #     'cookie': {
        #         'xq_a_token': '8940234022a656e1c577fe7c1e2791963527562b',
        #         'u': '1844895900'
        #     },
        #     'User-Agent': 'Xueqiu Android 11.19',
        #     'category': '1'
        # }
        r = requests.get(url,
                         params={'category': '1'},
                         cookies={'xq_a_token': '8940234022a656e1c577fe7c1e2791963527562b', 'u': '1844895900'},
                         headers={'User-Agent': 'Xueqiu Android 11.19'}
                         )
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()['data']['category'] == 1
