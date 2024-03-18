#!/usr/bin/python3
""" Web Flask app that returns list of states from DB """

from flask import Flask, render_template, jsonify
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(error=None):
    """ Removes each database session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def all_states():
    """ Returns a list of cities by state objects """
    states = storage.all(State)
    state_list = [v.to_dict() for v in states.values()]
    sorted_list = sorted(state_list, key=lambda x: x['name'])
    render = render_template('7-states_list.html', state_list=sorted_list)
    return render


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
