from flask import Flask, render_template
from flask_moment import Moment
from datetime import  datetime


app = Flask(__name__)

moment=Moment(app)

@app.route('/help/<time>')
def help(time):
    return  render_template("help.html",current_time=datetime.utcnow())


@app.route('/')
def index():
    return render_template("index2.html")


@app.route('/user/<name>')
def user(name):
    return render_template('user2.html', name=name)

@app.route('/ifelse/<username1>')
def ifelse(username1):
    return render_template("ifelse2.html", name=username1)


@app.route('/base/<use>')
def base(use):
    return render_template("base2.html", name=use)


@app.route('/rebase/<reuse>')
def rebase(reuse):
    return render_template("rebase.html", name=reuse)

if __name__ == '__main__':
    app.run(debug=True)
