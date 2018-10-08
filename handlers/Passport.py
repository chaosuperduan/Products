from .BaseHandler import BaseHandler
import logging


class IndexHandler(BaseHandler):
    @property
    def db(self):
        return self.application.db
    @property
    def redis(self):
        return self.application.redis

    def get(self):
        # self.write("hello")
        logging.debug("debug msg")
        logging.info("info msg")
        logging.warning("warming msg")
        print("msg")

        pass