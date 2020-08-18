import sqlite3

import click
from flask import Flask, render_template, request, jsonify, redirect, url_for, current_app, g
from flask.cli import with_appcontext
from . import db

app = Flask(__name__)
db.init_app(app)


DATABASE = 'database/database.db'


# def get_db():
#     db = getattr(Flask, '_database', None)
#     if db is None:
#         db = Flask._database = sqlite3.connect(DATABASE)
#     return db


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)



# def create_db():
#     c = db_conn().cursor()
#     c.execute("""DROP TABLE IF EXISTS songs;""")
#     table = """CREATE TABLE test(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     );
#     """
#     c.execute(table)
#     c.close()
#     return True


def db_conn():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn


# def my_form_post():
#     text = request.form['u']
#     processed_text = text.upper()
#     return processed_text


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
        #return redirect(url_for("user", usr=user))
        conn = db_conn()
        conn.cursor().execute('INSERT INTO test (name) VALUES("testname")')
    else:
        return render_template("public/login.html")


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



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    
if __name__ == "__main__":
    app.run(debug=True)