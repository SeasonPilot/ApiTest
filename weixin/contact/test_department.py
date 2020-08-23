# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/20 20:25
# 文件名：test_department.py.py
# 开发工具：PyCharm
import json
import logging
import time

import pytest
import requests

from weixin.contact.department import Department
from weixin.contact.token import WeiXin


class TestDepartment:
    # 在部门ID：1 下面创建多个部门
    def test_create_depth(self, token):
        for i in range(14):
            data = {
                "name": "广州研发中心" + str(time.time())[:10],  # 这里要转换成str
                "parentid": 1,
            }
            r = Department.creat(token, data)
            logging.debug(r)

    # 在部门ID：1 下面递归创建14个部门
    def test_create_depth1(self, token):
        parentid = 1

        for i in range(14):
            data = {
                "name": "第十期_seveniruby_" + str(parentid) + str(time.time())[:10],
                "parentid": parentid,
            }

            r = Department.creat(token, data)
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"] == 0

    # 获取部门列表
    def test_get_department(self, token):
        r = Department.list(token)
        logging.debug(json.dumps(r, indent=2))
        print(type(json.dumps(r, indent=2)))

    # 从ID最大的部门开始 删除部门
    def test_delete_department(self, token):
        for i in range(45):
            r = Department.delete(token, i)

    # 更新部门信息
    def test_put_department(self, token):
        data = {
            "id": 2,
            "name": "广州研seaosn gasfasjkfla发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = Department.update(token, data)

    @pytest.mark.parametrize(
        "name", [
            "广州研发中心",
            "東京アニメーション研究所",
            "도쿄 애니메이션 연구소",
            "معهد طوكيو للرسوم المتحركة",
            "東京動漫研究所"
        ]
    )
    def test_create_order(self, name, token):
        data = {
            "name": name,
            "parentid": 1,
            "order": 1,
        }
        r = Department.creat(token, data)
        logging.debug(r)
        assert r["errcode"] == 0
