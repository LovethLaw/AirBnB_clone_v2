#!/usr/bin/python3
"""Flask Initilization"""
from flask import Flask, render_template
from models import storage
from models.state import State
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


@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_route(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    odd_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of states and cities"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name())
    return render_template('7-states_list.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
