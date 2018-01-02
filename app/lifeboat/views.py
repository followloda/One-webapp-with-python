from flask import Flask, send_file
import os
from lifeboat import app



@app.route("/hello")
def hello():
    return "Hello World from Flask"


@app.route("/")
def main():
    index_path = os.path.join(app.static_folder, 'index.html')
    return send_file(index_path)
