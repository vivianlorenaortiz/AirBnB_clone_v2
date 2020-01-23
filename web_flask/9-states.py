#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def show_state(id=None):
    if id is not None:
        id = 'State.'+id
    return render_template(
        '9-states.html', states=storage.all("State"), state_id=id)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
