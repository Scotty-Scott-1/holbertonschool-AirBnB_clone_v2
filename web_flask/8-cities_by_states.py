#!/usr/bin/python3
""" a module that starts an app in flask. Has 2 routes"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def hello():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(error):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
