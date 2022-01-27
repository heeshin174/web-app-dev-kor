#!pip install Flask-SQLAlchemy
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# __file__ refer to main.py
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# set up the database location and configure the track modification settings
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" +os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRAC_MOODIFICATIONS"] = False

# create the database and pass our app in
db=SQLAlchemy(app)

# create model class
class Student(db.Model):
    __tablename__="students"

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text)
    grade=db.Column(db.Integer)

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __repr__(self):
        return f"Student {self.name} got {self.grade} on midterm exam"

	