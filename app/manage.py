from lifeboat import app,db
from flask_script import Manager
from lifeboat.models import User

manager = Manager(app)


"""
--数据库创建测试--
使用如下命令：
    python manage.py init_database

"""
@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    #创建测试用户
    for i in range(0,100):
        db.session.add(User("user"+str(i),"123456"))
    db.session.commit()
if __name__ == "__main__":
    manager.run()