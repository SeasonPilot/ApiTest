# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/23 21:33
# 文件名：department.py.py
# 开发工具：PyCharm
import requests


class Department:
    @classmethod
    def creat(cls, token, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                             params={"access_token": token},
                             json=dict,
                             ).json()

    @classmethod
    def list(cls, token, id=1, ):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                            params={"access_token": token,
                                    "id": id,
                                    }
                            ).json()

    @classmethod
    def delete(cls, token, i):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                            params={"access_token": token,
                                    "id": 45 - i
                                    }
                            )

    @classmethod
    def update(cls, token, data):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                             params={"access_token": token,
                                     # "id": 3
                                     },
                             json=data
                             )
