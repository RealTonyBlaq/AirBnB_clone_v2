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
def all_states_by_cities():
    """ Returns a rendered list of cities by state objects """
    states = [v.to_dict() for v in storage.all(State).values()]
    cities = [v.to_dict() for v in storage.all(City).values()]
    sorted_states = sorted(states, key=lambda x: x['name'])
    sorted_cities = sorted(cities, key=lambda x: x['name'])
    sorted_list = []
    for state in sorted_states:
        new = []
        for city in sorted_cities:
            if state['id'] == city['state_id']:
                new.append(city)
        sorted_list.append({"state_id": state['id'],
                            'state_name': state['name'], 'cities': new})
    return render_template('8-cities_by_states.html', a_list=sorted_list)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
