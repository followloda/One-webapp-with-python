from app.lifeboat import app


if __name__ == "__main__":
    #Only for debugging while developing
    #app.run(host='0.0.0.0', debug=True, port=80)
    app.run(host='127.0.0.1', debug=True, port=8080)
