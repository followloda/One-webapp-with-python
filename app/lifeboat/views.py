from flask import Flask, send_file,redirect,render_template
import os
from lifeboat import app,db
from lifeboat.models import User



@app.route("/hello")
def hello():
    return "Hello World from Flask"

@app.route("/hello/<int:user_id>/")
def head_img(user_id):
    user = User.query.get(user_id)
    if user == None:
        return redirect("/")
    return render_template("img.html",img = user.head_url,username =user.username)

@app.route("/")
def main():
    return render_template("index.html")
