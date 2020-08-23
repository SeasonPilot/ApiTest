# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/20 22:26
# 文件名：test_user.py
# 开发工具：PyCharm
import logging
import time

import pystache
import requests
from weixin.contact.token import WeiXin
from weixin.contact.user import User
from weixin.contact.utils import Utils


class TestUser:
    depart_id = 1

    # 创建成员
    def test_create_user(self):
        uid = str(time.time())
        # data 的类型为<class 'dict'>，所以传参类型为dict时用json。传参类型为str时用data
        data = {
            "userid": uid,
            "name": uid,
            "mobile": uid[:10] + "1",
            "department": self.depart_id,
        }
        print(type(data))
        r = User().create(dict=data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 获取部门成员
    def test_userlist(self):
        r = User().list()
        logging.debug(r)
        assert r["errcode"] == 0

    # 使用模板创建成员
    def test_creat_by_real(self):
        uid = str(time.time()).replace(".", "")[:11]
        # parse()返回值类型为str，所以data类型也是str,不是json。
        # 所以传参类型为dict时用json。传参类型为str时用data
        data = Utils().parse(template_path="user_create.json",
                             dict=
                             {"name": "Season",
                              "userid": uid,
                              "title": "校长",
                              "email": uid + "111@qq.com",
                              "mobile": uid
                              }
                             )
        # 增加编码格式
        data = data.encode("UTF-8")
        r = User().create(data=data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 模板使用练习
    def test_create_by_template_practice(self):
        # print(pystache.render("Hello {{name}} {{#has}}  word {{value}} {{/has}}",
        #                       {"name": "season", "has": [1, 2, 3], "value": "pilot"})
        #       )
        print(pystache.render("Hello {{name}} {{#has}}  word {{value}} {{/has}}",
                              {"name": "season",
                               "has": [
                                   {"value": "pilot"},
                                   {"value": "p"},
                                   {"value": "i"},
                                   {"value": "l"},
                                   {"value": "o"},
                               ]
                               }
                              )
              )
