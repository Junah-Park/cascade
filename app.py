from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/next')
def hello():
    return render_template("public/next.html")