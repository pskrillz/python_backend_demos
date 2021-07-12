from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv



# creating a simple flask application that uses data from the db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')

# links an instance of the database with the flask application
db = SQLAlchemy(app)


# creating a datamodel (a table) using sqlalchemy ORM
# "By inheriting from db.Model, we map from our classes to tables via SQLAlchemy ORM"
class Person(db.Model):

    #by default it is named lowercase class name but can customize this with:
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
    return 'Hello World'

# run using FLASK_APP=demo2-flask-helllo-world.py FLASK_DEBUG=true flask run
# debug addition allows live reload