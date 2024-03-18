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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def city_by_states(id):
    """ Returns a rendered list of cities by state objects """
    states = [v.to_dict() for v in storage.all(State).values()]
    if id:
        for obj in states:
            if obj['id'] == id:
    my_states = sorted(states, key=lambda x: x['name'])
    return render_template('9-states.html', states_list=my_states)
    

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
