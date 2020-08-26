# _*_ coding:utf-8 _*_
# 作者：Season
# 时间：2020/8/26 19:53
# 文件名：media.py
# 开发工具：PyCharm
# import requests
#
#
# class Media:
#     @classmethod
#     def upload(cls, pig_token):
#         return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload",
#                              params={"access_token": pig_token,
#                                      "type": type},
#                              ).json()
#
#     @classmethod
#     def get(cls, pig_token):
#         return requests.get("https://qyapi.weixin.qq.com/cgi-bin/media/get",
#                             params={"access_token": pig_token,
#                                     "media_id": "2G4x0J5v2OfvBaZHodGxgtmn3R2E1F4mrebloUDUdVADy8gA3vMUvq9JGOKA14qbn"},
#                             ).json()
#
#     @classmethod
#     def uploadimg(cls, pig_token):
#         return requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg",
#                              params={"access_token": pig_token},
#                              ).json()
