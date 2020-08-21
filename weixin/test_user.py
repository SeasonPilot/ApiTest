# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/20 22:26
# 文件名：test_user.py
# 开发工具：PyCharm
import requests

from weixin.token import WeiXin


class TestUser:
    def test_create_user(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": WeiXin().get_token()},
                          )
