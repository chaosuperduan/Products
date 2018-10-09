# coding:utf-8
import logging
from BaseHandler import BaseHandler
from utils.captcha.captcha import captcha
import re
from constants import PIC_CODE_EXPIRES_SECONDS

class ImageCodeHandler(BaseHandler):

    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        # if pre_code_id:
        #     try:
        #         self.redis.delete("")
        #     except Exception as e:
        #         logging.error(e)

        name,text,image = captcha.generate_captcha()

        # self.write(image)
        # self.set_header("Content-Type", "image/jpg")
        try:
            self.redis.setex("ImageCode_%s" %code_id,constants.PIC_CODE_EXPIRES_SECONDS,text)

        except Exception as e:
            logging.error(e)
            self.write("")
        else:
            self.set_header("Content-Type","image/jpg")
            self.write(image)





