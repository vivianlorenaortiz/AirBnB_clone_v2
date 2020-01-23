#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    storage.close()


@app.route('/cities_by_states')
def show_cities_by_state():
    return render_template(
        '8-cities_by_states.html', states=storage.all("State").values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
