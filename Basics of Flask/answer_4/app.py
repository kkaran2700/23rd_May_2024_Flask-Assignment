# 4. Create a Flask app with a form that accepts user input and displays it.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("mainpage.html")

@app.route('/process_input', methods=['POST', 'GET'])
def process_input():
    d = request.form.get('user_input')
    return f"You entered: {d}"

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5004)
