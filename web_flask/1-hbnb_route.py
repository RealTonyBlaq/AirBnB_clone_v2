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


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
