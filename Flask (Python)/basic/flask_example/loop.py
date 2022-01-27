# We also have access to control flow syntax in our 
# templates such as for loops and if statements.
# We will use {%. %} syntax for these.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    days = ["Sunday", "Monday", "Tuesday","Wednesday","Thursday", "Friday", "Saturday"]
    return render_template('exercise3.html', days=days)

if __name__ == '__main__':
    app.run()