# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/20 22:26
# 文件名：test_user.py
# 开发工具：PyCharm
import json
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
    def test_create_user(self, token):
        # data 的类型为<class 'dict'>，所以传参类型为dict时用json。传参类型为str时用data
        data = {
            "userid": Utils.uid(),
            "name": Utils.uid(),
            "mobile": Utils.uid(),
            "department": self.depart_id,
        }
        print(type(data))
        r = User().create(token, dict=data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 读取成员
    def test_get_user(self, token):
        r = User.get(token, 1)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # 更新成员
    def test_update_user(self, token):
        data = {
            "userid": 1,
            "name": Utils.uid(),
            "mobile": Utils.uid()
        }
        r = User.update(token, data)
        logging.debug(json.dumps(r, indent=2))
        logging.debug(type(r))
        assert r["errcode"] == 0

    # 删除成员
    def test_delete_user(self, token):
        userid = 1
        r = User.delete(token, userid)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # 批量删除成员
    def test_batchdelete(self, token):
        userlist = {
            "useridlist": [
                "15981728465",
                "zhangsan",
                "15981837285"
            ]
        }
        r = User.batchdelete(token, userlist)
        logging.debug(r)
        # 字符串类型转换为字典类型要用eval，不能用dict
        assert r["errcode"] == 0

    # 获取部门成员
    def test_userlist(self, token):
        r = User().simplelist(token)
        logging.debug(r)
        assert r["errcode"] == 0

    # 使用模板创建成员
    def test_creat_by_real(self, token):
        # parse()返回值类型为str，所以data类型也是str,不是json。
        # 所以传参类型为dict时用json。传参类型为str时用data
        data = Utils().parse(template_path="user_create.json",
                             dict=
                             {"name": "Season",
                              "userid": Utils.uid(),
                              "title": "校长",
                              "email": Utils.uid() + "@qq.com",
                              "mobile": Utils.uid()
                              }
                             )
        # 增加编码格式
        data = data.encode("UTF-8")
        r = User().create(token, data=data)
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

    # 获取部门成员详情
    def test_userlist_details(self, token):
        department_id = 1
        fetch_child = 0
        r = User.list(token, department_id=department_id, fetch_child=fetch_child)
        logging.debug(r)
        assert r["errcode"] == 0

    # 邀请成员
    def test_invite(self, token):
        data = {
            "user": ["15981841772", "15981841772", "1598102560.458127"],
            "party": [2],
        }

        r = User.invite(token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 获取加入企业二维码
    def test_get_join_qrcode(self, token):
        r = User.qrcode(token)
        logging.debug(r)
        assert r["errcode"] == 0

    # 获取企业活跃成员数
    def test_active(self, token):
        data = {
            "date": time.strftime("%Y-%m-%d", time.localtime())
        }
        r = User.active(token, data)
        logging.debug(r)
        assert r["errcode"] == 0
