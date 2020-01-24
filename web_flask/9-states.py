#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
strict_slashes = False


@app.teardown_appcontext
def teardown_session(self):
    storage.close()


@app.route("/states")
def hello9half():
    """ if no id passed """
    statesArr = list(storage.all("State").values())
    statesArr.sort(key=lambda statesArr: statesArr.name)
    return render_template("9-states.html", states=statesArr, state_id=None)


@app.route("/states/<state_id>")
def hello9(state_id=None):
    """ sets up the cities in states """
    statesArr = storage.all("State")
    if state_id:
        state = statesArr.get("State.{}".format(state_id))
        if state:
            statesArr = [state]
        else:
            statesArr = []
    else:
        statesArr = list(statesArr.values())
    statesArr.sort(key=lambda statesArr: statesArr.name)
    for state in statesArr:
        state.cities.sort(key=lambda statesArr: statesArr.name)
    return render_template(
        "9-states.html", states=statesArr, state_id=state_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
