# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/24 22:52
# 文件名：test_application.py
# 开发工具：PyCharm

# 获取应用
import json
import logging

from weixin.contact.application import Application


class TestApplication:

    # 获取指定的应用详情
    def test_get(self, pig_token):
        r = Application.get(pig_token)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # 获取access_token对应的应用列表
    def test_list(self, pig_token):
        r = Application.list(pig_token)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # 设置应用
    def test_set(self, pig_token):
        data = {"agentid": 1000004,
                "name": "租场",
                "description": "养租场！"}
        r = Application.set(pig_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 创建菜单
    def test_create(self, pig_token):
        data = {
            "button": [
                {
                    "type": "click",
                    "name": "今日歌曲",
                    "key": "V1001_TODAY_MUSIC"
                },
                {
                    "name": "菜单",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "搜索",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "click",
                            "name": "赞一下我们",
                            "key": "V1001_GOOD"
                        }
                    ]
                }
            ]
        }
        r = Application.create(pig_token, data)
        logging.debug(json.dumps(r, indent=2))
        assert r["errcode"] == 0

    # 获取菜单
    def test_get_menu(self, pig_token):
        r = Application.get_menu(pig_token)
        logging.debug(r)
        assert r["errcode"] == 0

    # 删除菜单
    def test_delete(self, pig_token):
        r = Application.delete(pig_token)
        logging.debug(r)
        assert r["errcode"] == 0
