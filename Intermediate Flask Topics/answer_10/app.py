# 10. Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "About Page"

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/cause500')
def cause_500():
    raise Exception("This is a test for the 500 error page.")


if __name__ == '__main__':
    app.run(debug=True)
