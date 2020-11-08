
import jwt
from datetime import datetime, timedelta

from jwt import PyJWTError

from Config import config

payload = {  # jwt设置过期时间的本质 就是在payload中 设置exp字段, 值要求为格林尼治时间
    "user_id": 1,
    'exp': datetime.utcnow() + timedelta(seconds=30)
}

screct_key = "test"
# 生成token
token = jwt.encode(payload, key=config.SCRECT_KEY, algorithm='HS256')
print("Bearer "+str(token, encoding="utf8"))
try:
    data = jwt.decode(token, key=config.SCRECT_KEY, algorithms='HS256')
    print(data)
except PyJWTError as e:
    print("jwt验证失败: %s" % e)