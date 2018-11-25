#coding:utf-8
from qiniu import Auth,put_file,etag,urlsafe_base64_decode
import qiniu.config

#需要填写你的Access Key 和Secret Key
access_key = 'uzc59bVURbUbazey9vrexXKocNKBUN8NuLijk57N'
secret_key = '-9lenw28jU2REojvGkcsEPWk5Nm9V2HIVqb5Nkts'

def storage(image_data):
    if not image_data:
        return None
    # 构建鉴权对象。
    q = Auth(access_key, secret_key)
    # 需要上传的空间。

    bucket_name = 'ihome'
    # 上传到七牛后保存的文件名
    # key = 'my_python-logo.png'
    # 生成上传的token.
    token = q.upload_token(bucket_name, None, 3600)
    # 要上传的文件路径。
    # localfile = './sync/bb.jpg'
    ret, info = put_file(token, None, image_data)
    print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    return ret['key']




