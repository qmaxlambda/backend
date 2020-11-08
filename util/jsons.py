import datetime

from flask import jsonify, make_response


def js_ret(code=None, msg=None, data=None):
    """
    return json 返回参数处理
    code :状态码
    data:返回结果
    """
    rt_data = {
        "code": code,
        "msg": msg,
        "data": data

    }
    jss = jsonify(rt_data)
    return make_response(jss, 200)

def json_serial(obj):
    # 处理日期格式问题
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, datetime.date)):
        if isinstance(obj,datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return obj.soformat()
    raise TypeError ("Type %s not serializable" % type(obj))