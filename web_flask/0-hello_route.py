#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask

# Create an instance of the Flask app
app = Flask(__name__)

# Defining the Route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!' whe accessing the root URL.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
