import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///ncaa.db")

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
def homepage():
    with open('/tmp/conferences.json', 'r') as f:
        conferences = json.loads(f.read())

    teams = []
    for conference in conferences:
        a = conference['abbreviation']
        with open('/tmp/' + a + '.json', 'r') as g:
            t = json.loads(g.read())
            teams += t

    return render_template('index.html', conferences=conferences, teams=teams)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
