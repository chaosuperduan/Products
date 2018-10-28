#coding=gbk

#coding=utf-8
from CCPRestSDK import REST
import ConfigParser
import logging

#���ʺ�
accountSid= '8aaf070866235bc501665edf9f821d06';

#���ʺ�Token
accountToken= 'ad7b29bb94c74e4983f4ae3e213c3d93';

#Ӧ��Id
appId='8aaf070866235bc501665edf9fd41d0c';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='https://app.cloopen.com:8883';

#����˿�
serverPort='8883';
#REST�汾��
softVersion='2013-12-26';

# ˵����
class CCP(object):

    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @staticmethod
    def instance():
        if not hasattr(CCP, "_instance"):
            CCP._instance = CCP()
        return CCP._instance

    def sendTemplateSMS(self, to, datas, tempId):
        try:
            result = self.rest.sendTemplateSMS(to, datas, tempId)
        except Exception as e:
            logging.error(e)
            raise e

        # print result
        # for k, v in result.iteritems():
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)
        if result.get("statusCode") == "000000":
            return True
        else:
            return False

ccp = CCP.instance()

if __name__ == "__main__":
    ccp = CCP.instance()
    ccp.sendTemplateSMS("18666208770", ["1234", 5], 1)
