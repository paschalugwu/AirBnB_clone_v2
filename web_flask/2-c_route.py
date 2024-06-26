#!/usr/bin/python3
"""
Task 2: Starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when accessing the root URL.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when accessing the /hbnb URL.
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays 'C' followed by the value of <text>.
    Underscores i <text> are replaced by spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
