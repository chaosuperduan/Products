# coding:utf-8
from tornado.web import  RequestHandler
import logging

class BaseHandler(RequestHandler):
    """
    handle基类
    """
    def prepare(self):
        pass
    def write_error(self, status_code, **kwargs):
        pass
    def set_header(self, name, value):
        pass
    def initialize(self):
        pass
    def on_finish(self):
        pass






