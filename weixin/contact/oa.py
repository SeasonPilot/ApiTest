# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/26 20:45
# 文件名：oa.py
# 开发工具：PyCharm
import requests


class OA:
    @classmethod
    def get(cls, checkin_token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata",
                             params={"access_token": checkin_token},
                             json=dict
                             ).json()

    @classmethod
    def getcheckinoption(cls, checkin_token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckinoption",
                             params={"access_token": checkin_token},
                             json=dict
                             ).json()
