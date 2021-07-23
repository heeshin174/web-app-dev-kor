# "Jinja" templating will let us directly insert variables 
# from our Python code to the HTML file.
# The syntax for inserting a variable is: 
# {{variable_name}

# We also have access to control flow syntax in our 
# templates such as for loops and if statements.
# We will use {%. %} syntax for these.

#Filters
# Filters are a great way to quickly change/edit a variable passed to a template.
#  {{ name }}
# mahmut
# {{ name | capitalize }} 
# Mahmut


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name="shin hee"
    return render_template('exercise2.html', my_name=name)

if __name__ == '__main__':
    app.run()