# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/11 20:32
# 文件名：test_requests.py
# 开发工具：PyCharm
import logging
import requests
import json
import pytest
# from hamcrest import *
from hamcrest import assert_that, any_of, has_item, equal_to, close_to, has_items, all_of
from jsonpath_ng import parse, jsonpath
import jsonpath
from jsonschema import validate


class TestRequests:
    logging.basicConfig(level=logging.INFO)

    def test_xuqiu(self):
        r = requests.get('https://testerhome.com/api/v3/topics.json?limit=2')
        logging.info(r)
        logging.info(json.dumps(r.json(), indent=2))

    def test_xueqiu_quote(self):
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json'
        # 这样写是错误的
        # params = {
        #     'cookie': {
        #         'xq_a_token': '8940234022a656e1c577fe7c1e2791963527562b',
        #         'u': '1844895900'
        #     },
        #     'User-Agent': 'Xueqiu Android 11.19',
        #     'category': '1'
        # }
        r = requests.get(url,
                         params={'category': '1'},
                         cookies={'xq_a_token': '8940234022a656e1c577fe7c1e2791963527562b', 'u': '1844895900'},
                         headers={'User-Agent': 'Xueqiu Android 11.19'}
                         )
        # logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))
        assert r.json()['data']['category'] == 1
        assert r.json()['data']['stocks'][0]['name'] == '创业板'
        logging.info(jsonpath.jsonpath(r.json(), '$.data.stocks[0].name'))
        # 取 symbol == "00030" 的股票  的名称，返回的是列表
        logging.info(jsonpath.jsonpath(r.json(), '$.data.stocks[?(@.symbol == "00030")].name'))
        # 去上面列表的第0个元素
        logging.info(jsonpath.jsonpath(r.json(), '$.data.stocks[?(@.symbol == "00030")].name')[0])
        assert jsonpath.jsonpath(r.json(), '$.data.stocks[?(@.symbol == "00030")].name')[0] == '万隆控股集团'
        assert_that(jsonpath.jsonpath(r.json(), '$.data.stocks[?(@.symbol == "00030")].name')[0],
                    equal_to('万隆控股集团'), "比较上市代码与名字")

        # 第一种写法
        # find(r.json()),find括号里要是一个json格式的数据,是接口返回的数据
        # parse括号里面是要从接口中取回的数据表达式
        # 返回的是i项目中 Key对应的value
        # stocks_name = [i.value for i in parse('$.data.stocks[*].name').find(r.json())]
        # print(stocks_name)

        # 第二种写法 （推荐）
        stocks_name = jsonpath.jsonpath(r.json(), '$.data.stocks[*].name')
        logging.info(jsonpath.jsonpath(r.json(), '$.data.stocks[*].name'))

        assert_that(stocks_name,
                    any_of(
                        has_item('创业板'),
                        has_item('券商ETF')
                    )
                    )

    def test_xueqiu_list_schema(self):
        url = 'https://stock.xueqiu.com/v5/stock/portfolio/stock/list.json'
        r = requests.get(url,
                         params={'category': '1'},
                         cookies={'xq_a_token': '8940234022a656e1c577fe7c1e2791963527562b', 'u': '1844895900'},
                         headers={'User-Agent': 'Xueqiu Android 11.19'}
                         )
        logging.info(json.dumps(r.json(), indent=2))
        schema = json.load(open("list_schema.json", encoding='utf-8'))
        validate(instance=r.json(), schema=schema)

    def test_hamcrest(self):
        assert_that(0.1 * 0.1, close_to(0.01, 0.1))
        assert_that(['a', 'b', 'c'], has_item('a'))
        assert_that(['a', 'b', 'c'], has_items('b', 'a'))
        assert_that(
            ['a', 'b', 'c'],
            any_of(
                has_items('b', 'd'),
                has_items('b', 'c')
            )
        )
        assert_that(
            ["a", "b", "c"],
            all_of(
                has_items("b", "d"),
                has_items("b", "c")
            )
        )

    def test_schema(self):
        schema = {
            "type": "object",
            "properties": {
                "price": {"type": "number"},
                "name": {"type": "string"},
            },
        }
        validate(instance={"name": "Eggs", "price": "34.99"}, schema=schema)
