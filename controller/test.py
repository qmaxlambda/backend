from flask import Blueprint, request
test = Blueprint('test',__name__)




@test.route('/helloworld')
def hello_world():
    """
        用户注册
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
    return "1"

