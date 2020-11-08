# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 下午 04:59
# @Author  : Mason
# @Email   : 295146397@qq.com
# @File    : oss.py
# @Software: PyCharm
import json
import os
import oss2
from flask import request, Blueprint
from Config import config
from util.jsons import js_ret

oss_bp = Blueprint('oss',__name__)

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', config.ACCESSKEY_ID)
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', config.ACCESSKEY_SCRECT)
bucket_name = os.getenv('OSS_TEST_BUCKET', config.BUCKET_NAME)
endpoint = os.getenv('OSS_TEST_ENDPOINT', config.ENDPOINT)


# 确认参数
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

# 创建Bucket对象
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

@oss_bp.route('/update',methods=["GET", "POST"])
def update():
    # 上传文件到服务器
    file = request.files.get('file')
    if file is None:
        return js_ret(0,'没有检索到文件')
    else:
        # 上传文件到阿里云OSS
        res = bucket.put_object(file.filename, file)
        if res.status == 200:
            # 上传成功，获取文件带签名的地址，返回给前端
            url = bucket.sign_url('GET', file.filename, 60)
            data = {
                "url":url
            }
            return js_ret(1,"",data)
