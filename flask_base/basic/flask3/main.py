# Forms with Flask
# We will be using/learning flask_wtf and wtforms packages

# 1. configure a secret key for security
# 2. create a WTForm Class
# 3. will set up a View Function
#    Add methods= [‘GET’, ‘POST’]
#    Create an instance of Form Class
#    Handle Form submission

# pip install flask, flask_wtf, wtforms
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "oursecretkey"

class MyForm(FlaskForm):
    customer = StringField("What is your customer id?")
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    customer=False
    form = MyForm()
    if form.validate_on_submit():
        customer = form.customer.data
        form.customer.data= ''
    return render_template('main.html', form=form, customer=customer)

if __name__ == '__main__':
    app.run()