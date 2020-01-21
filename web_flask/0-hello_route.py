#!/usr/bin/python3
"""
Write a scrip that starts a Flasak web application.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
