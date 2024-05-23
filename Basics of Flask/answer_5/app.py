# 5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, render_template, request
import logging as log

log.basicConfig(filename='userinfo.log', level=log.INFO, format= '%(message)s - %(asctime)s - %(levelname)s')

app = Flask(__name__)

@app.route('/')
def home():
    log.info("opening home page")
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def user_data():

    userinfo = {
    'user_name' : request.form.get('username'), 
    'e-mail' : request.form.get('email'),
    'pw': request.form.get('password')}

    log.info("user_name is %s", userinfo['user_name'])
    log.info("e-mail is %s", userinfo['e-mail'])
    log.info("password is %s", userinfo['pw'])

    with open('user_info.txt', 'a') as file:
        file.write(f"Username: {userinfo['user_name']}, Email: {userinfo['e-mail']}, Password: {userinfo['pw']}\n")

    return f"user information of {userinfo['user_name']} is saved in the database"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)