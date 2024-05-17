#!/usr/bin/python3
"""Strorage is an instance of FileStorage or DBStorage"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def citites_by_states():
    """Displays a HTML page with a list of states and cities"""
    states = sorted(storage.all("State").values(), key=lambda x: x.name())
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
