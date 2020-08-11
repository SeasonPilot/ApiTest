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
