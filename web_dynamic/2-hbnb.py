#!/usr/bin/python3
"""
AirBnB static HTML template integration with a Flask app
"""
import uuid
from flask import Flask, render_template, url_for
from models import storage

# Installs the required configurations on Flask.
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    defines a teardown function that, upon completion
    of each request, closes the database connection.
    """
    storage.close()


@app.route('/2-hbnb/')
def hbnb_filters(the_id=None):
    """
    requests for templates includs cities, states, and amenities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('2-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
