#!/usr/bin/python3
""" a module that starts an app in flask. Has 2 routes"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello2():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
