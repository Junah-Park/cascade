import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("public/login.html")
# def my_form_post():
#     text = request.form['u']
#     processed_text = text.upper()
#     return processed_text

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

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

if __name__ == "__main__":
    app.run(debug=True)