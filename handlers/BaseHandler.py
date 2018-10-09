# coding:utf-8
from tornado.web import  RequestHandler
import logging

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
        pass
    def write_error(self, status_code, **kwargs):
        pass
    # def set_header(self, name, value):
    #     pass
    def initialize(self):
        pass
    def on_finish(self):
        pass






