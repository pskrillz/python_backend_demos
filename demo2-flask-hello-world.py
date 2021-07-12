from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv



# creating a simple flask application that uses data from the db


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING')

# links an instance of the database with the flask application
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World'

# run using FLASK_APP=demo2-flask-helllo-world.py FLASK_DEBUG=true flask run
# debug addition allows live reload