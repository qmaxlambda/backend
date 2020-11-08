from flask import Flask
from flask_sqlalchemy import SQLAlchemy



from flasgger import Swagger
from Config import config
from controller.oss import oss_bp
from controller.test import test
from controller.user import user_bp

app = Flask(__name__)
#读取配置
app.config.from_object(config)

#swagger

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = config.SWAGGER_TITLE    # 配置大标题
swagger_config['description'] = config.SWAGGER_DESC    # 配置公共描述内容
swagger_config['host'] = config.SWAGGER_HOST    # 请求域名

# swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
# swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
# swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
# swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'
Swagger(app, config=swagger_config)

# 注册蓝图
app.register_blueprint(test , url_prefix='/test')
app.register_blueprint(user_bp , url_prefix='/user')
app.register_blueprint(oss_bp , url_prefix='/oss')

db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ = "wx_user"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(16), unique=True)
#     mobile = db.Column(db.Integer, unique=True)
#     # 给Role类创建一个uses属性，关联users表。
#     # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
#     # users = db.relationship('User', backref="role")
#
#     # 相当于__str__方法。
#     def __repr__(self):
#         return "Role: %s %s" % (self.id, self.name)
#     def to_json(self): # ---------------------
#         dict = self.__dict__
#         if "_sa_instance_state" in dict:
#             del dict["_sa_instance_state"]
#         return dict

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    # try:
    #     user1 = User()
    #     user1.name = 'aaa'
    #     db.session.add(user1)
    #     # 最后插入完数据一定要提交
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     raise e

    app.run(port=3030)
