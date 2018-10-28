
import os
from handlers import Passport ,VerifyCode
from tornado.web import StaticFileHandler
urls = [(r"/",Passport.IndexHandler),
            (r"/api/imagecode",VerifyCode.ImageCodeHandler),
        (r'/api/smscode',VerifyCode.SMSCodeHandle),
        (r"/(.*)",StaticFileHandler,dict(path =os.path.join(os.path.dirname(__file__),"html"),default_filename ="index.html")),


]