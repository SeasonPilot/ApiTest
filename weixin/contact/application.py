# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/24 22:51
# 文件名：application.py
# 开发工具：PyCharm
import requests


class Application:
    agentid = 1000004

    @classmethod
    def get(cls, pig_token):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/get",
                            params={"access_token": pig_token,
                                    "agentid": cls.agentid}
                            ).json()

    @classmethod
    def list(cls, pig_token):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/agent/list",
                            params={"access_token": pig_token}
                            ).json()

    @classmethod
    def set(cls, pig_token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/agent/set",
                             params={"access_token": pig_token},
                             json=dict
                             ).json()

    @classmethod
    def create(cls, pig_token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create",
                             params={"access_token": pig_token,
                                     "agentid": cls.agentid},
                             json=dict
                             ).json()

    @classmethod
    def get_menu(cls, pig_token):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/get",
                            params={"access_token": pig_token,
                                    "agentid": cls.agentid},
                            ).json()

    @classmethod
    def delete(cls, pig_token):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/menu/delete",
                            params={"access_token": pig_token,
                                    "agentid": cls.agentid},
                            ).json()
