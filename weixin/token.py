# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/18 23:05
# 文件名：testuser.py
# 开发工具：PyCharm
import logging

import requests
import yaml


class WeiXin:
    logging.basicConfig(level=logging.DEBUG)

    def get_token(self):
        conf = yaml.safe_load(open("weixin.yaml"))
        # 这里的debug是小写
        logging.debug(conf['env'])

        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={
                             'corpid': conf['env']['corpid'],
                             'corpsecret': conf['env']['Secret']
                         }
                         ).json()
        # 这里要return 的是 token
        return r["access_token"]
