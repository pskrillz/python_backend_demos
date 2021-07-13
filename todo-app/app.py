from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv


# to run:
# FLASK_APP=app.py flask run

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CONNECTION_STRING_TODO')
db = SQLAlchemy(app)





# this is the modesl (M)
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

db.create_all()

# This is the controller (C)
@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.form['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    jsonify({
        'description': todo.description
    })
    return redirect(url_for('index', description=description))
    

