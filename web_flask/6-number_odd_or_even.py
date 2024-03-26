#!/usr/bin/python3
"""Task 6"""

# Import Flask and render_template from Flask
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Configure Jinja to remove unnecessary whitespace in templates
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Define a route for the root URL
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

# Define a route for /hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"

# Define a route for /c/<text>
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

# Define a route for /python and /python/<text>
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>
    Replaces any underscores in <text> with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

# Define a route for /number/<int:n>
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)

# Define a route for /number_template/<int:n>
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer.
    Displays the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)

# Define a route for /number_odd_or_even/<int:n>
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer.
    States whether <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)


# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0")
