#!/usr/bin/python3
""" a module that starts an app in flask. Has 2 routes"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage



app = Flask(__name__)

@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def hello(id=None):
    key = ""
    state_exists = False
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    if id is not None:
        key = "state." + id
        for state in states:
            if state.id == id:
                state_ob = state
                state_exists = True

        if state_exists:
            return render_template("9-states.html", state=state_ob, key=key, found=True)
        else:
            return render_template("9-states.html", found=False)
    else:
        return render_template("9-states.html", states=states, list_states=True)

@app.teardown_appcontext
def teardown(error):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
