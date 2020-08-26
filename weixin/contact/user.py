# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/23 16:07
# 文件名：user.py.py
# 开发工具：PyCharm
import requests

from weixin.contact.token import WeiXin


# 所有return 都要转换成json格式！！！！！！！！！


class User:
    def create(self, token, data=None, dict=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                             params={"access_token": token},
                             json=dict,
                             data=data
                             ).json()

    # 设置默认值更加方便，并设置**kwargs留后路
    def simplelist(self, token, department_id=1, fetch_child=0, **kwargs):
        return requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            # "department_id": 1 要写到params里，不是json参数里。  “department_id”在请求地址中
            params={"access_token": token,
                    "department_id": department_id,
                    "fetch_child": fetch_child
                    },
        ).json()

    @classmethod
    def get(cls, token, userid=1):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",
                            params={"access_token": token,
                                    "userid": userid}
                            # 要转换成json格式
                            ).json()

    @classmethod
    def update(cls, token, data):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/update",
                             params={"access_token": token},
                             json=data
                             ).json()

    @classmethod
    def delete(cls, token, userid):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete?",
                            params={"access_token": token,
                                    "userid": userid},
                            ).json()

    @classmethod
    def batchdelete(cls, token, userlist):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?",
                             params={"access_token": token},
                             json=userlist
                             ).json()

    @classmethod
    def list(cls, token, department_id=1, fetch_child=0):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/list?",
                            params={"access_token": token,
                                    "department_id": department_id,
                                    "fetch_child": fetch_child
                                    },
                            # 要转换成json格式
                            ).json()

    @classmethod
    def invite(cls, token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/batch/invite",
                             params={"access_token": token},
                             json=dict
                             ).json()

    @classmethod
    def qrcode(cls, token, size_type=1):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/corp/get_join_qrcode",
                            params={"access_token": token,
                                    "size_type": size_type}
                            ).json()

    @classmethod
    def active(cls, token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/get_active_stat",
                             params={"access_token": token, },
                             json=dict
                             ).json()
