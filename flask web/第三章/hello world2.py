from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/sbzgj")
def sb():
    return "张国健是一个大傻逼"


if __name__ == "__main__":
    app.run()
