from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING_TODO')
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

db.create_all()