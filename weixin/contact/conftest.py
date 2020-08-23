# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/23 20:16
# 文件名：conftest.py
# 开发工具：PyCharm
import pytest

from weixin.contact.token import WeiXin


@pytest.fixture
def token():
    return WeiXin().get_token()
