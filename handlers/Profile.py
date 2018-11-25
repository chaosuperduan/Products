from utils.common import require_logined
from .BaseHandler import BaseHandler
import logging
import pymysql
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









