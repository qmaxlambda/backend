import json


class Base():
    msg = ''
    data = ''
    code = 0
    def __init__(self, data,msg,code):
        self.data = data
        self.code = code
        self.msg = msg
    def __str__(self):
        return json.dumps({
            'code': self.code,
            'msg': self.msg,
            'data': self.data,
        }, default=lambda o: o.__dict__, sort_keys=True)
    def __repr__(self):
        return repr((self.code, self.msg, self.data))

class A():
    name ="a"
    age = 12
    def __init__(self, name,age):
        self.name = name
        self.age = age



a = A(name ='123',age = 12)


base = Base(code =1,data=a,msg ='')
print(base)

