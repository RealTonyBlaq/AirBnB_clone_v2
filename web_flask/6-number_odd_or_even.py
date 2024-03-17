#!/usr/bin/python3
""" Script starts a Web Flask App """

from flask import abort, Flask, make_response, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """ Returns a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def sub():
    """ Returns a string when this path is accessed """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Returns a string + text passed to the url """
    if "_" in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text="is cool"):
    """ Returns a string + text passed """
    if "_" in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ Returns a string plus the number passed """
    try:
        number = int(n)
        return "{} is a number".format(number)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def template(n):
    """ Displays an HTML page if n is a number else """
    try:
        number = int(n)
        render = render_template('5-number.html', number=number)
        return render
    except ValueError:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def template2(n):
    """ """


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
