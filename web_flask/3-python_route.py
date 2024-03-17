#!/usr/bin/python3
""" Script starts a Web Flask App """

from flask import Flask


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


@app.route('/python/<text>', strict_slashes=False)
def py_route(text="is cool"):
    """ Returns a string + text passed """
    if "_" in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)
    

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
