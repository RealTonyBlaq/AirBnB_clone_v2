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
    objs = [ob.to_dict() for ob in states.values()]
    render = render_template('7-states_list.html', state_list=objs)
    return render


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
