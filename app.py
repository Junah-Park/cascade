import sqlite3
from flask import request
from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)

# DATABASE = 'database/database.db'
# # def get_db():
# #     db = getattr(Flask, '_database', None)
# #     if db is None:
# #         db = Flask._database = sqlite3.connect(DATABASE)
# #     return db




# def create_db():
#     with sqlite3.connect(DATABASE) as connection:
#         c = connection()
#         c.execute("""DROP TABLE IF EXISTS songs;""")
#         table = """CREATE TABLE test(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL);"""
#         c.execute(table)
#         connection.commit()
#         c.close()
#     return True

# def db_conn():
#     with sqlite3.connect(DATABASE) as connection:
#         return connection

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
        # db_conn().execute('''INSERT INTO test(name) VALUES('testname')''')
        # db_conn().commit()
        data="success"
        print("yay")
    return jsonify(data)

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(Flask, '_database', None)
#     if db is not None:
#         db.close()