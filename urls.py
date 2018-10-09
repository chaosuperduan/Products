

from handlers import Passport ,VerifyCode

urls = [(r"/",Passport.IndexHandler),
            (r"/api/imagecode",VerifyCode.ImageCodeHandler)

]