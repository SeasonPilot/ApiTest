# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/23 16:07
# 文件名：user.py.py
# 开发工具：PyCharm
import requests

from weixin.contact.token import WeiXin


class User:
    def create(self, data=None, dict=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                             params={"access_token": WeiXin().get_token()},
                             json=dict,
                             data=data
                             ).json()

    # 设置默认值更加方便，并设置**kwargs留后路
    def list(self, department_id=1, fetch_child=0, **kwargs):
        return requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            # "department_id": 1 要写到params里，不是json参数里。  “department_id”在请求地址中
            params={"access_token": WeiXin().get_token(),
                    "department_id": department_id,
                    "fetch_child": fetch_child
                    },
        ).json()
