#!/usr/bin/python3
"""Flask web"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def display_num(n):
    if isinstance(n, int):
        return n + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('index.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
