#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    # Display numbers in the range with newline characters, ending with a newline
    numbers = "\n".join(str(num) for num in range(parameter)) + "\n"
    return numbers, 200, {'Content-Type': 'text/plain'}

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Undefined (division by zero)'
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"

    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
