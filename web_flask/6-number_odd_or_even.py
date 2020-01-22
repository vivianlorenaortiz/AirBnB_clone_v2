#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    tex = text.replace("_", " ")
    return 'c {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text="is cool"):
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_numbertemplate(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
