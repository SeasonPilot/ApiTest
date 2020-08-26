# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/25 21:06
# 文件名：test_message.py
# 开发工具：PyCharm
import logging

from weixin.contact.message import Message


class TestMessage:
    # 发送应用消息
    def test_send(self, pig_token):
        data = {
            "touser": "@all",
            "toparty": "@all",
            "totag": "@all",
            "msgtype": "text",
            "agentid": 1000004,
            "text": {
                "content": "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        r = Message.send(pig_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 创建群聊会话
    def test_create_appchat(self, pig_token):
        data = {
            "name": "hahah",
            # "owner": "userid1",
            "userlist": ["15981841772", "15981867041", "ZhaoWeiChen"],
            "chatid": "1512"
        }
        r = Message.create_appchat(pig_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 修改群聊会话
    def test_update(self, pig_token):
        data = {
            "chatid": "1512",
            "name": "你覅算法网购文",
            "owner": "ZhaoWeiChen",
            # "add_user_list": ["userid1", "userid2", "userid3"],
            # "del_user_list": ["userid3", "userid4"]
        }
        r = Message.update(pig_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 获取群聊会话
    def test_get(self, pig_token):
        r = Message.get(pig_token)
        logging.debug(r)
        assert r["errcode"] == 0

    # 应用推送消息
    def test_appchat_send(self, pig_token):
        data = {
            "chatid": "1512",
            "msgtype": "text",
            "text": {
                "content": "你的快递已到\n请携带工卡前往邮件中心领取"
            },
            "safe": 0
        }
        r = Message.appchat_send(pig_token, data)
        logging.debug(r)
        assert r["errcode"] == 0

    # 查询应用消息发送统计
    def test_get_statistics(self, pig_token):
        r = Message.get_statistics(pig_token)
        logging.debug(r)
        assert r["errcode"] == 0
