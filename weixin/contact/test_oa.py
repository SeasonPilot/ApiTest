# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/26 20:45
# 文件名：test_oa.py
# 开发工具：PyCharm
import logging
import time

from weixin.contact.oa import OA


class TestOA:
    def test_get(self, checkin_token):
        data = {
            "opencheckindatatype": 3,
            "starttime": str(time.time())[:10],
            "endtime": str(time.time())[:10],
            "useridlist": ["ZhaoWeiChen", "15981841772"]
        }
        r = OA.get(checkin_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    def test_getcheckinoption(self, checkin_token):
        data = {
            "datetime": str(time.time())[:10],
            "useridlist": ["ZhaoWeiChen", "15981841772"]
        }
        r = OA.getcheckinoption(checkin_token, data)
        logging.debug(r)
        assert r["errcode"] == 0
