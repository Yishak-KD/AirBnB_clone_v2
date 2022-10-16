#!/usr/bin/python3
"""Flask web"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    new = text.replace("_", " ")
    return "C " + new


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    new = text.replace("_", " ")
    return "Python " + new

if __name__ == "__main__":
    app.run(host='0.0.0.0')
