import sqlite3
from flask import request
from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)

DATABASE = 'database/database.db'

# def get_db():
#     db = getattr(Flask, '_database', None)
#     if db is None:
#         db = Flask._database = sqlite3.connect(DATABASE)
#     return db

def create_db():
    c = db_conn().cursor()
    c.execute("""DROP TABLE IF EXISTS songs;""")
    table = """CREATE TABLE test(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """
    c.execute(table)
    c.close()
    return True

def db_conn():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/next')
def hello():
    return render_template("public/next.html")

@app.route('/test', methods=['GET','POST'])
def test():
    data = "failure"
    if request.method == 'GET' or request.method == 'POST':
        conn = db_conn()
        if(conn == None):
            create_db()
        conn.cursor().execute('INSERT INTO test (name) VALUES("testname")')
        data="success"
        print("yay")
    return jsonify(data)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(Flask, '_database', None)
    if db is not None:
        db.close()