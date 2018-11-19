# coding:utf-8

import uuid
import logging
import json
import config
# session = Session(request_handler=self)
# session.sesson_id = "abcdesfsdfs"
#
# #第一次访问或者出错。
# session.data = {}
#
# #{}

# class Session(object):
#     def __init__(self,request_handler):
#         logging.error("这儿执行了")
#         self.request_handler = request_handler
#         self.session_id = self.request_handler.get_secure_cookie("session_id")
#         if not self.session_id:
#             self.session_id = uuid.uuid4().get_hex()
#             self.data = {}
#             logging.error(self.session_id)
#         else:
#             try:
#                 data = self.redis.get("sess_%s"%self.session_id)
#             except Exception as e:
#                 logging.error(e)
#                 raise e
#
#         if not data:
#             logging.error("fuuk")
#             self.data = {}
#         else:
#             self.data = json.load(data)
#
#     def save(self):
#         json_data = json.dump(self.data)
#         try:
#             self.redis.setx("sess_%s"%self.sesson_id,config.session_expires_seconds,json_data)
#         except Exception as e:
#             logging.error(e)
#             raise Exception("save session faild")
#         else:
#             self.request_handler.set_secure_cookie("session_id",self.sesson_id)
#
#
#     def clear(self):
#         self.request_handler.clear_cookie("session_id")
#         try:
#             self.redis.delete("sess_%s"%self.session_id)
#         except Exception as e:
#             logging.error(e)



class Session(object):
    """"""
    def __init__(self, request_handler_obj):

        # 先判断用户是否已经有了session_id
        self._request_handler = request_handler_obj
        self.session_id = request_handler_obj.get_secure_cookie("session_id")

        # 如果不存在session_id,生成session_id
        if not self.session_id:
            self.session_id = uuid.uuid4().hex
            self.data = {}
            request_handler_obj.set_secure_cookie("session_id", self.session_id)

        # 如果存在session_id, 去redis中取出data
        else:
            try:
                json_data = request_handler_obj.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                raise e
            if not json_data:
                self.data = {}
            else:
                self.data = json.loads(json_data)

    def save(self):
        json_data = json.dumps(self.data)
        try:
            self._request_handler.redis.setex("sess_%s" % self.session_id,
                                             config.session_expires_seconds, json_data)
        except Exception as e:
            logging.error(e)
            raise e

    def clear(self):
        try:
            self._request_handler.redis.delete("sess_%s" % self.session_id)
        except Exception as e:
            logging.error(e)
        self._request_handler.clear_cookie("session_id")


"""
class xxxxhandler(RequestHandler):
    def post(self):

        session = Session(self)
        session.session_id
        session.data["username"] = "abc"
        session.data["mobile"] = "abc"
        session.save()

    def get(self):
        session = Session(self)
        session.data["username"] = "def"
        session.save()



    def get(self):
        session = Session(self)
        session.clear()

        session.clear()

redis中的数据：
key:    session_id
value:  data
"""










