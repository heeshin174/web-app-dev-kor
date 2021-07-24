import re
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

class InfoForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    messages = StringField("message")
    submit = SubmitField('Submit')

@app.route('/', methods=["GET", "POST"])
def base():
    form = InfoForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session["pasword"] = form.password.data
        msgs = []
        count = 0
        last_char = form.password.data[-1]
        m = re.search(r'\d$', last_char)
        if form.password.data.islower() == True:
            msgs.append("You did not use an uppercase character.")
            count += 1

        if form.password.data.isupper() == True:
            msgs.append("You did not use an lowercase character.")
            count += 1

        if m is None:
            msgs.append("You did not end your username with a number")
            count += 1

        if count > 0:
            session['messages'] = msgs
            return redirect(url_for("index", msgs=msgs))
        else:
            return redirect(url_for("report"))
    return render_template("base.html", form=form)

@app.route('/index')
def index():
    msgs = session['messages']
    return render_template('index.html', msgs=msgs)

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run()