#!/usr/bin/python3
"""Flask Initilization"""
from flask import Flask
# from web_flask import app

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<str:text>", strict_slashes=False)
def python_route(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_route(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
