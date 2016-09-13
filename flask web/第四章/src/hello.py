from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run(debug=True)


