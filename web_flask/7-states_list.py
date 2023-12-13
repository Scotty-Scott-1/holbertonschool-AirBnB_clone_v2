#!/usr/bin/python3
""" a module that starts an app in flask. Has 1 routes"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello():
    """get a list of states"""
    states = list(sorted(storage.all(State).values(), key=lambda x: x.name))
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(error):
    """close and reload file and db storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
