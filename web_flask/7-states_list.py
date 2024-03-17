#!/usr/bin/python3
""" Web Flask app that returns list of states from DB """

from flask import abort, Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Removes each database session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def all_states():
    """ Returns a list of state objects """
    states = storage.all(State)
    for
    
