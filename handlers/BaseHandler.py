# coding:utf-8
from tornado.web import RequestHandler,StaticFileHandler
import tornado.web
import logging
import json
from tornado.web import StaticFileHandler
from utils.session import Session
class BaseHandler(RequestHandler):

    """
    handle基类
    """

    @property
    def db(self):
        """作为RequestHandler对象的db属性"""
        return self.application.db

    @property
    def redis(self):
        """作为RequestHandler对象的redis属性"""
        return self.application.redis
    def set_default_headers(self):
        """设置默认json格式"""
        self.set_header("Content-Type", "application/json; charset=UTF-8")
    def prepare(self):
        self.xsrf_token
        #预解析json
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}




    def get_current_user(self):
        """判断用户是否登录"""
        self.session = Session(self)
        return self.session.data








    def write_error(self, status_code, **kwargs):
        pass
    # def set_header(self, name, value):
    #     pass
    def initialize(self):
        pass
    def on_finish(self):
        pass



# class StaticFileBaseHandler(StaticFileHandler):
#     """自定义静态文件处理类, 在用户获取html页面的时候设置_xsrf的cookie"""
#     def __init__(self, *args, **kwargs):
#         super(StaticFileBaseHandler, self).__init__(*args, **kwargs)
#         self.xsrf_token

class StaticFileBaseHandler(tornado.web.StaticFileHandler):
    """自定义静态文件处理类, 在用户获取html页面的时候设置_xsrf的cookie"""
    logging.error("静态方法开始执行")
    def __init__(self, *args, **kwargs):
        logging.error("静态方法开始执行")
        super(StaticFileBaseHandler, self).__init__(*args, **kwargs)
        self.xsrf_token


