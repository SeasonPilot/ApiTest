# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/23 19:48
# 文件名：utils.py
# 开发工具：PyCharm
import logging

import pystache


class Utils:
    # 使用字典替换user_create.json文件中的{{}}中的内容
    def parse(self, template_path, dict):
        template = "".join(open(template_path, encoding="utf-8").readlines())
        logging.debug(template)
        # 返回值类型为str
        print(type(pystache.render(template, dict)))
        return pystache.render(template, dict)
