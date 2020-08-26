# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/25 21:05
# 文件名：message.py
# 开发工具：PyCharm
import requests


class Message:
    agentid = 1000004

    @classmethod
    def send(cls, pig_token, data):
        return requests.post(" https://qyapi.weixin.qq.com/cgi-bin/message/send",
                             params={"access_token": pig_token},
                             json=data
                             ).json()

    @classmethod
    def create_appchat(cls, pig_token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/appchat/create",
                             params={"access_token": pig_token},
                             json=dict
                             ).json()

    @classmethod
    def update(cls, pig_token, data):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/appchat/update",
                             params={"access_token": pig_token},
                             json=data
                             ).json()

    @classmethod
    def get(cls, pig_token):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/appchat/get",
                            params={"access_token": pig_token,
                                    "chatid": "1512"
                                    }
                            ).json()

    @classmethod
    def appchat_send(cls, pig_token, data):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/appchat/send",
                             params={"access_token": pig_token},
                             json=data
                             ).json()

    @classmethod
    def get_statistics(cls, pig_token):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/get_statistics",
                             params={"access_token": pig_token},
                             json={
                                 "time_type": 0
                             }
                             ).json()
