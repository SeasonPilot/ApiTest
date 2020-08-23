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


class TestUser:
    depart_id = 1

    # 创建成员
    def test_create_user(self):
        uid = str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "mobile": uid[:10] + "1",
            "department": self.depart_id,
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": WeiXin().get_token()},
                          json=data
                          ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    # 获取部门成员
    def test_userlist(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            # "department_id": 1 要写到params里，不是json参数里。  “department_id”在请求地址中
            params={"access_token": WeiXin().get_token(),
                    "department_id": 1,
                    "fetch_child": 1
                    },
        ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    # 使用模板创建成员
    def test_creat_by_template(self):
        data = self.get_user({"name": "Season", "title": "校长", "email": str(time.time())[:10] + "111@qq.com"})
        # 增加编码格式
        data = data.encode("UTF-8")
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": WeiXin().get_token()},
                          data=data
                          ).json()
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

    # 使用字典替换user_create.json文件中的{{}}中的内容
    def get_user(self, dict):
        template = "".join(open("user_create.json", encoding="utf-8").readlines())
        logging.debug(template)
        print(type(pystache.render(template, dict)))
        return pystache.render(template, dict)

    # 测试 get_user
    def test_get_user(self):
        logging.debug(self.get_user({"name": "Season", "title": "校长", "email": str(time.time())[:10] + "111@qq.com"}))
