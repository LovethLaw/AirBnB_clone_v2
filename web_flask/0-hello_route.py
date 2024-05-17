#!/usr/bin/python3
"""Flask Initilization"""
from flask import Flask
# from web_flask import app

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Flask Home page"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
