from app import db


class user(db.Model):
    __tablename__ = "wx_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    mobile = db.Column(db.Integer, unique=True)
    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    # users = db.relationship('User', backref="role")

    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s" % (self.id, self.name)
    def to_json(self): # ---------------------
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

res = user.query
print(res)
