#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Root view: show application title in an h1."""
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_string(text):
    """Print the string to the console and return it in the response body."""
    print(text)
    return text


@app.route('/count/<int:number>')
def count(number):
    """Return numbers from 0..number-1 each on its own line, trailing newline included."""
    lines = ''.join(f"{i}\n" for i in range(number))
    return lines


@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    """Perform a math operation between two numbers and return the result as text.

    Supported operations: +, -, *, div (division), % (modulo)
    """
    # Convert numeric strings to ints when possible
    try:
        a = int(num1)
        b = int(num2)
    except ValueError:
        # fallback to float conversion if ints are not suitable
        a = float(num1)
        b = float(num2)

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == 'div':
        # true division
        result = a / b
    elif operation == '%':
        result = a % b
    else:
        return 'Unsupported operation', 400

    # Return integer-like results without a decimal when appropriate
    if isinstance(result, float) and result.is_integer():
        # but tests expect '1.0' for divisions that produce float, so only
        # coerce to int for non-division ops. We'll special-case 'div'.
        if operation == 'div':
            return str(float(result))
        return str(int(result))

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
