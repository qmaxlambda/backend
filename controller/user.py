
import jwt
from flask import Blueprint, request, json
from datetime import datetime, timedelta

from jwt import PyJWTError

from Config import config
from util.jsons import js_ret


user_bp = Blueprint('user_bp',__name__)

"""
    用户获取token
    ---
    tags:
      - 用户相关接口
    description:
        用户注册接口，json格式
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: 用户注册
          required:
            - username
            - password
            - inn_name
          properties:
            username:
              type: string
              description: 用户名.
            password:
              type: string
              description: 密码.
            inn_name:
              type: string
              description: 客栈名称.
            phone:
              type: string
              description: 手机号.
            wx:
              type: string
              description: 微信.

    responses:
      201:
          description: 注册成功


          example: {'code':1,'message':注册成功}
      406:
        description: 注册有误，参数有误等

    """
@user_bp.route('/gettoken',methods=["GET", "POST"])
def GetToken():
    name = request.form.get("name")
    payload = {  # jwt设置过期时间的本质 就是在payload中 设置exp字段, 值要求为格林尼治时间
        "user_id": 1,
        "name":name,
        'exp': datetime.utcnow() + timedelta(seconds=3000)

    }
    token = jwt.encode(payload, key=config.SCRECT_KEY, algorithm='HS256')
    token = "Bearer "+str(token, encoding="utf8")
    tokenjson ={
        "token":token
    }

    return js_ret(1,"",tokenjson)



@user_bp.route('/',methods=["GET", "POST"])
def Hello():
    print('请求来的时候111')
    return "Hello World"

#中间件
@user_bp.before_request
def process():
    token = request.headers.get("Authorization")
    if request.path == "/user/gettoken":  # 判断路径,如果是/login,就pass
        return None
    else:
        if token is None:
            return js_ret(0,"no token")
        else :
            try:
                token = bytes(token[7:], encoding = "utf8")
                data = jwt.decode(token, key=config.SCRECT_KEY, algorithms='HS256')
                return js_ret(1,"",data)
            except PyJWTError as e:
                return js_ret(0, "jwt验证失败: %s" % e)
    return js_ret(0,"no token")



# @user_bp.route('/query',methods=["GET", "POST"])
# def Query():
#     if request.method == 'GET':
#         name = request.form.get("name")
#         page_size = int(request.form.get("count"))
#         page_index = int(request.form.get("page"))
#         res = user.query.paginate(page_index, page_size, False)
#         de =[]
#         for r in res.items:
#             de.append(r.to_json())
#         return js_ret(1,'',de)
#     if request.method == 'POST':
#         return "null"
#     return "null"