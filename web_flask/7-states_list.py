#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    state_list = storage.all("State")
    state_arr = state_list.values()
    sorted_arr = []
    for state in sorted(state_arr, key=lambda k: k.name):
        sorted_arr.append(state)
    return render_template('7-states_list.html', state_list=sorted_arr)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
