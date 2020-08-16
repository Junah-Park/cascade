import sqlite3
from flask import Flask
from flask import render_template
app = Flask(__name__)
DATABASE = '/path/to/database.db'

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/next')
def hello():
    return render_template("public/next.html")


def get_db():
    db = getattr(Flask, '_database', None)
    if db is None:
        db = Flask._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(Flask, '_database', None)
    if db is not None:
        db.close()