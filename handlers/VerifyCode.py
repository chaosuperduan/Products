# coding:utf-8
import logging
from BaseHandler import BaseHandler
from utils.captcha.captcha import captcha
import re
import constants
import random
import utils.response_code
import json
from constants import PIC_CODE_EXPIRES_SECONDS
from constants import SMS_CODE_EXPIRES_SECONDS
from utils.response_code import RET
from lib.yuntongxun.CCP import ccp
class ImageCodeHandler(BaseHandler):

    def get(self):
        code_id = self.get_argument("codeid")
        pre_code_id = self.get_argument("pcodeid")
        if pre_code_id:
            try:
                self.redis.delete("")
            except Exception as e:
                logging.error(e)

        name,text,image = captcha.generate_captcha()
        self.set_header("Content-Type", "image/jpg")

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





class SMSCodeHandle(BaseHandler):
    def post(self):

        mobile = self.json_args.get("mobile")
        logging.error(mobile)
        imge_code_id = self.json_args.get("image_code_id")
        logging.error(imge_code_id)
        imge_code_text = self.json_args.get("image_code_text")
        logging.error(imge_code_text)
        if not all((mobile, imge_code_id, imge_code_text)):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="参数缺失"))
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode=RET.PARAMERR, errmsg="手机号格式错误"))
        try:
            real_image_code_text = self.redis.get('image_code_%s',imge_code_id)
            # logging.error(real_image_code_text)
        except Exception as e:
            logging.error(e)
            logging.error(real_image_code_text)
            return self.write(dict(errno=RET.DBERR,errmsg="查询出错"))
        if not real_image_code_text:
            return  self.write(dict(errno=RET.NODATA,errmsg="验证码过期"))
        # 转小写
        if real_image_code_text.lower() != imge_code_text.lower:
            return self.write(dict(errno=RET.DATAERR,errmsg="验证码错误"))
        #生成随机验证码。并存储
        sms_code = "%04d"%random.randint(0,9999)
        logging.error(sms_code)
        try:
            self.redis.setex("sm_code_%s"%mobile,SMS_CODE_EXPIRES_SECONDS,sms_code)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.DBERR,errmsg="生成短信验证码错误"))



        #发送短信。
        try:
            ccp.sendTemplateSMS(mobile,[sms_code,constants.SMS_CODE_EXPIRES_SECONDS],1)
        except Exception as e:
            logging.error(e)
            return self.write(dict(errno=RET.THIRDERR),errmsg="发送失败")

        self.write(dict(errno=RET.OK,ermsg="ok"))


        #不成功:
        #返回错误信息:













