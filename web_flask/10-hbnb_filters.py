#!/usr/bin/python3
""" a module that starts an app in flask. Has 2 routes"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """get a list of states"""
    states = storage.all(State).values()
    states_sort = sorted(states, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    amenities_sort = sorted(amenities, key=lambda x: x.name)
    return render_template(
        "10-hbnb_filters.html", states=states_sort, amenities=amenities_sort)


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
