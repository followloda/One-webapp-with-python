from lifeboat import db
import random

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.head_url = "https://pic1.zhimg.com/v2-66cbf7a2989ad9ffe8e24d69b711e094_xl.jpg"

    def __repr__(self):
        return '<User %d %s>' % (self.id,self.username)