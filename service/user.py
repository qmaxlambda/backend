from app import db



def CreateUser(User):
    try:
        db.session.add(User)
        # 最后插入完数据一定要提交
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
