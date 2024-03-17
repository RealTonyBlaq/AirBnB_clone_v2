#!/usr/bin/python3
""" Script starts a Web Flask App """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root()
