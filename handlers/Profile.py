# coding:utf-8
from utils.common import require_logined
from .BaseHandler import BaseHandler
import logging
from utils.response_code import RET
from utils.image_storage import storage
import constants

# from utils.commons import required_login
import pymysql

#上传头像。

class AvatarHandler(BaseHandler):
    @require_logined
    def post(self):
        files = self.request.files.get("avatar")
        if not files:
            return self.write(dict(errcode=RET.PARAMERR, errmsg="未传图片"))
        avatar = files[0]["body"]
        cur = self.db.cursor()

        #调用七牛上传图片。
        try:
            file_name = storage(avatar)
            logging.error("djkjfkj")
            logging.error(file_name)
            logging.error("djkjfkj")


            logging.error(file_name)
        except Exception as e :
            logging.error(e)
            return self.write(dict(errno=RET.THIRDERR,errmsg="上传失败"))
        #从session数据取出user_id
        user_id = self.session.data["user_id"]
        #保持图片名（图片url)到数据。
        sql = "update ih_user_profile set up_avatar=%s where up_user_id=%s"
        try:
            row_count = cur.execute(sql,(file_name,user_id))
        except Exception as e:
            logging.error(e)
            return self.write(dict(errcode=RET.DBERR, errmsg="保存错误"))
        self.write(dict(errcode=RET.OK, errmsg="保存成功", data="%s%s" % (constants.QINIU_URL_PREFIX, file_name)))


class ProfileHandler(BaseHandler):




    @require_logined
    def get(self):
        # self.session



        user_id = self.session.data["user_id"]
        logging.error("huoquyonghuid")
        logging.error(user_id)

        cur = self.db.cursor()
        sql = "select up_name,up_mobile ,up_avatar from ih_user_profile where up_user_id = %s"

        try:
            ret = cur.execute(sql,user_id)

        except Exception as e:
            logging.error(e)
            return self.write({"errno":1,"errmsg":"no data"})
        result = cur.fetchone()
        if result[2]:
            img_url = ""
        else:
            img_url = None
        self.write({"errno":0,"errmsg":"ok","data":{"user_id":user_id,"name":result[0]},
                    "mobile":result[1],"avatar":img_url
                    })









