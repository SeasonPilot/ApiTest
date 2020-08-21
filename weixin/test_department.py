# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/20 20:25
# 文件名：test_department.py.py
# 开发工具：PyCharm
import datetime
import json
import logging
import time

import requests

from weixin.token import WeiXin


class TestDepartment:
    # 在部门ID：1 下面创建多个部门
    def test_create_depth(self):
        for i in range(14):
            data = {
                "name": "广州研发中心" + str(time.time())[:10],  # 这里要转换成str
                "parentid": 1,
            }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": WeiXin().get_token()},
                              json=data,
                              ).json()
            logging.debug(r)

    # 在部门ID：1 下面递归创建14个部门
    def test_create_depth1(self):
        parentid = 1

        for i in range(14):
            data = {
                "name": "第十期_seveniruby_" + str(parentid) + str(time.time())[:10],
                "parentid": parentid,
            }

            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": WeiXin().get_token()},
                              json=data,
                              # proxies={"https": "http://127.0.0.1:8080",
                              #          "http": "http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            parentid = r["id"]

    # 获取部门列表
    def test_get_department(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": WeiXin().get_token(),
                                 "id": 1,
                                 }
                         ).json()
        logging.debug(json.dumps(r, indent=2))

    # 从ID最大的部门开始 删除部门
    def test_delete_department(self):
        for i in range(45):
            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/delete",
                             params={"access_token": WeiXin().get_token(),
                                     "id": 45 - i
                                     }
                             )

    # 更新部门信息
    def test_put_department(self):
        data = {
            "id": 2,
            "name": "广州研seaosn gasfasjkfla发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/update",
                          params={"access_token": WeiXin().get_token(),
                                  # "id": 3
                                  },
                          json=data
                          )
