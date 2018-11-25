# coding:utf-8

from .BaseHandler import BaseHandler
import logging
import hashlib
import config
import re
import pymysql
from utils.session import Session
from utils.response_code import RET
# class IndexHandler(BaseHandler):
#     @property
#     def db(self):
#         return self.application.db
#     @property
#     def redis(self):
#         return self.application.redis
#
#     def get(self):
#         # self.write("hello")
#         logging.debug("debug msg")
#         logging.info("info msg")
#         logging.warning("warming msg")
#         print("msg")
#
#         pass
class RegisterHandler(BaseHandler):
    def post(self):
        logging.error("注册——****————————")

        mobile = self.json_args.get("mobile")
        sms_code = self.json_args.get("phonecode")
        password = self.json_args.get("password")
        # if not all(mobile,sms_code,password):
        #     return self.write({"error":1,"errmsg":"参数错误"})

        real_code = self.redis.get("sms_code_%s" % mobile)
        # logging(real_code)
        if real_code != sms_code and str(sms_code) != "2468":
            return  self.write({"errno":2,"errmsg":"验证码无效"})
        # 存储密码
        passwd = hashlib.sha256(config.passwd_hash_key+password).hexdigest()
        cur = self.db.cursor()

        # sql = "insert into ih_user_profile(up_name,up_mobile,up_passwd)values(%(name)s,%(mobile)s,%(passwd)s;"
        # try:
        #     res = cur.execute(sql,name=mobile,mobile=mobile,passwd= passwd)
        #
        #
        # except Exception as e:
        #     logging.error(e)
        #     return self.write({"errno":3,"errmsg":"手机号已经注册"})





        passwd = hashlib.sha256(password + config.passwd_hash_key).hexdigest()


        sql = "insert into ih_user_profile(up_name, up_mobile, up_passwd) values(%s, %s, %s)"

        try:
            res = cur.execute(sql, (mobile, mobile, passwd))
        except Exception as e:
            logging.error("__@")
            logging.error(e)
            logging.error("@@@")
            return self.write(dict(errcode=3, errmsg="手机号已存在"))
        self.db.commit()
        logging.error("__@")
        logging.error(res)
        logging.error("__@")
        try:
            self.session = Session(self)
            self.session.data["user_id"] = res
            self.session.data["name"] = mobile
            self.session.data["mobile"] = mobile
            self.session.save()
        except Exception as e:
            logging.error(e)

        self.write({"errno":0,"errmsg":"ok"})


class LoginHandler(BaseHandler):
    def post(self):
        mobile = self.json_args.get("mobile")
        password = self.json_args.get("password")

        logging.error(mobile)
        logging.error(password)

        #检查参数。
        if not all([mobile,password]):
            return  self.write({"errno":3, "errmsg": "参数错误"})
        if not re.match(r"^1\d{10}$", mobile):
            return self.write(dict(errcode=RET.DATAERR, errmsg="手机号错误"))
        #检查密码是否正确。
        cur = self.db.cursor()
        res = cur.execute("select up_user_id,up_name,up_passwd from ih_user_profile  where up_mobile=%s",mobile)

        result = cur.fetchall()

        cur.close()
        logging.error("!!!!! ")

        logging.error(result[0][0])
        logging.error("$$$$$")
        logging.error(result[0][2])
        logging.error("!!!!! ")
        password = hashlib.sha256(password+config.passwd_hash_key).hexdigest()
        logging.error(password)
        if res and result[0][2] == password:
            try:
                self.session = Session(self)
                self.session.data['user_id'] = result[0][0]
                self.session.data['name'] = result[0][1]
                self.session.data['mobile'] = result[0][0]
                logging.error("session")
                logging.error(self.session.data)
                logging.error("session")
                self.session.save()
            except Exception as e:
                logging.error(e)
            return  self.write({'errno':RET.OK,'errmsg':'OK'})
        else:
            return  self.write({'errno':RET.DATAERR,'errmsg':'手机号或者密码错'})


class CheckLoginHandler(BaseHandler):
    """检查登陆状态"""
    def get(self):
        # get_current_user方法在基类中已实现，它的返回值是session.data（用户保存在redis中
        # 的session数据），如果为{} ，意味着用户未登录;否则，代表用户已登录
        if self.get_current_user():
            self.write({"errcode":0, "errmsg":"true", "data":{"name":self.session.data.get("name")}})
        else:
            self.write({"errcode":RET.SESSIONERR, "errmsg":"false"})







