class config(object):
    # 指定数据库的链接信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@127.0.0.1:3306/childimg"
    # 这个配置将来会被禁用,设置为True或者False可以解除警告信息,建议设置False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_TITLE = "Api文档"
    SWAGGER_HOST ="127.0.0.1"
    SWAGGER_DESC = ""
    SCRECT_KEY = "test"
    ACCESSKEY_ID = "LTAI4FeckSieCfKFAZidtngD"
    ACCESSKEY_SCRECT = "143btS0WbCocYTa3uk1DWScRA1cWHC"
    ENDPOINT = "oss-cn-shenzhen.aliyuncs.com"
    BUCKET_NAME = "imgtest123321"