from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,DateTimeField,
                     RadioField,SelectField,TextField, TextAreaField)
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["SECRET_KEY"] = "anothersecretkey"

class InfoForm(FlaskForm):
    department = StringField("What is your department?", validators=[DataRequired()])
    graduated = BooleanField("Did you Graduate?")
    degree = RadioField("Please choose your degree: ", choices=[("level_one", "Undergrad"),("level_two","Graduate")])
    job_choice = SelectField("Where do you want to work?", choices=[('job1', "industry"), ("job2", "Academia")])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['department'] = form.department.data
        session["graduated"] = form.graduated.data
        session["degree"] = form.degree.data
        session["job_choice"] = form.job_choice.data
        session["feedback"] =form.feedback.data
        return redirect(url_for("thankyou"))

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()