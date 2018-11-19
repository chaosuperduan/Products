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

class Session(object):
    def __init__(self,request_handler):
        logging.error("这儿执行了")
        self.request_handler = request_handler
        self.session_id = self.request_handler.get_secure_cookie("session_id")
        if not self.session_id:
            self.session_id = uuid.uuid4().get_hex()
            self.data = {}
        else:
            try:
                data = self.redis.get("sess_%s"%self.session_id)
            except Exception as e:
                logging.error(e)
                raise e

        if not data:
            self.data = {}
        else:
            self.data = json.load(data)

    def save(self):
        json_data = json.dump(self.data)
        try:
            self.redis.setx("sess_%s"%self.sesson_id,config.session_expires_seconds,json_data)
        except Exception as e:
            logging.error(e)
            raise Exception("save session faild")
        else:
            self.request_handler.set_secure_cookie("session_id",self.sesson_id)


    def clear(self):
        self.request_handler.clear_cookie("session_id")
        try:
            self.redis.delete("sess_%s"%self.session_id)
        except Exception as e:
            logging.error(e)











