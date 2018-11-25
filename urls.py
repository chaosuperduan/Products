# coding:utf-8
import os
from handlers import Passport ,VerifyCode,Profile

# from handlers.BaseHandler import StaticFileBaseHandler as StaticFileHandler
from tornado.web import StaticFileHandler
urls = [
        # (r"/",Passport.IndexHandler),
        (r"/api/imagecode",VerifyCode.ImageCodeHandler),
        (r"/api/login", Passport.LoginHandler),
        (r"/api/register", Passport.RegisterHandler),
        (r'/api/smscode',VerifyCode.SMSCodeHandle),
        (r"/api/profile", Profile.ProfileHandler), # 个人主页获取个人信息
        (r"/api/check_login", Passport.CheckLoginHandler), # 判断用户是否登录
        (r"/(.*)", StaticFileHandler,
        dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))

]