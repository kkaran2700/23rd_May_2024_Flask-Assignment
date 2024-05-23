# 3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask, request


app = Flask(__name__)

@app.route('/kkk')
def parameters():
    data =  request.args.get('name')
    return f" you searched for {data}"

@app.route('/add')
def add2nums():
    num1 =  request.args.get('num1')
    num2 =  request.args.get('num2')

    if num1 is None or num2 is None:
        return f"please enter both the numbers in the url"
    
    try:
        result = int(num1)+ int(num2)
        return f"The sum of {num1} and {num2} is {result}"
    except Exception as e:
        return f"exception is {e}"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)