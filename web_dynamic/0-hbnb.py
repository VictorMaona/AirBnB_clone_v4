#!/usr/bin/python3
"""
App for Flask that works with AirBnB static HTML template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# flask arrangement
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# start rendering the flask page
@app.teardown_appcontext
def teardown_db(exception):
    """
    calls after every request.close()  (deleted()) from
    the active SQLAlchemy session
    """
    storage.close()


@app.route('/0-hbnb/')
def hbnb_filters(the_id=None):
    """
    responds to requests for templates as cities, states and amenities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('1-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
