# 1. Create a Flask app that displays "Hello, World!" on the homepage.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
