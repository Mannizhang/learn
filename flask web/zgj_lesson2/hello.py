from flask import Flask,render_template
from flask import abort
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route("/")
def index():
    # user_agent = request.headers.get('User-Agent')
    # return "<h1>helloWorld, %s</h1>" % user_agent
    # return redirect('http://baidu.com')
    return  render_template("index.html")


@app.route("/user/<name>")
def user(name):

    return render_template('user.html',name = name)
    # if load_user(name):
    #     return "<h1>hello, %s!</h1>" % name
    # else:
    #     abort(404)
# return "<h1>hello, %s!</h1>" % name

@app.route("/ifelse/<userName>")
def ifelse(userName):

    return render_template("ifelse.html",name = userName)


@app.route("/list")
def list():
    list = ['f','u','c','k']
    return render_template("list.html", list = list)

@app.route("/macro")
def macro():
    return render_template("macro.html")

def load_user( id ):
    if int(id) == 123:

        return True
    return False



if __name__ == '__main__':
    app.run(debug=True)
