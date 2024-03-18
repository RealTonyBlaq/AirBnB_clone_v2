#!/usr/bin/python3
""" Web Flask app that returns list of states from DB """

from flask import Flask, render_template
from models.city import City
from models.state import State
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(error=None):
    """ Removes each database session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_by_states():
    """ Returns a rendered list of cities by state objects """
    

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
