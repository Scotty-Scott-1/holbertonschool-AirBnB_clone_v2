#!/usr/bin/python3
""" a module that starts an app in flask. Has 2 routes"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello2():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello3(text):
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def hello4(text="is_cool"):
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>", strict_slashes=False)
def hello5(n):
    return "{} is a number".format(int(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello6(n):
    numb = int(n)
    return render_template("5-number.html", num=numb)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
