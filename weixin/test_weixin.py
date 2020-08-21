# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/18 23:21
# 文件名：test_weixin.py
# 开发工具：PyCharm
from weixin.token import WeiXin


def test_token():
    print(WeiXin().get_token())
    assert test_token != ""
