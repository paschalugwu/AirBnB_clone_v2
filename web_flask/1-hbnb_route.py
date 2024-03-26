#!/usr/bin/python3
"""
Starts a Flask web application.
"""
# Import the necessary modules
from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)


# Define two routes using the @app.route decorator
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' when accessing the root URL.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when accessing the '/hbnb' URL
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
