# coding:utf-8
import tornado.web
import logging
import config
import constants
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import  define,options
from urls import urls
import pymysql
import redis
define("port",type=int,default=8000,help="run server on the given port")

# class Application(tornado.web.Application):
#     def __init__(self,*args,**kwargs):
#
#         super(Application,self).__init__(*args,**kwargs)
#         #直接采用字典解包
#         self.db = pymysql.Connect(**config.mysql_options)
#         # self.db = pymysql.Connection(host=config.mysql_options["host"],
#         #                              database=config.mysql_options["database"],
#         #                              user=config.mysql_options["user"],
#         #                              password=config.mysql_options["password"],
#         #                              charset=config.mysql_options["charset"])
#         self.redis = redis.StrictRedis(**config.redis_options)
#
#         # self.redis = redis.StrictRedis(
#         #
#         #     host=config.redis_options["host"],
#         #     port=config.redis_options["port"]
#         # )

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)


        self.db = pymysql.Connect(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)
        print(self.redis)



def main():

    # 设置日志级别

    options.logging = config.log_level
    # options.logging = ""
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()





    app  = Application(urls,**config.settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()




if __name__ == '__main__':
   main()

