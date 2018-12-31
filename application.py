import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
import json
from helpers import lookup

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


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/conferences")
def conferences():
    with open('/tmp/conferences.json', 'r') as f:
        conferences = json.loads(f.read())
    return jsonify(conferences)


@app.route("/schools", methods=['GET'])
def schools():
    with open('./resources/teams/conferences.json', 'r') as f:
        conferences = json.loads(f.read())
    schools = []
    for conference in conferences:
        a = conference['abbreviation']
        with open('./resources/teams/' + a + '.json', 'r') as g:
            t = json.loads(g.read())
            schools += t
    return jsonify(schools)


@app.route("/rosters", methods=['GET'])
def rosters():

    if 'school' in request.args:
        school = (request.args['school'])

    s1 = school.replace(" ", "_").replace("'", " ").replace(
        "&", "").replace("(", "").replace(")", "")

    with open('./resources/rosters/' + s1 + '.json', 'r') as f:
        roster = json.loads(f.read())

    return jsonify(roster)


@app.route("/schedules", methods=['GET'])
def schedules():

    if 'school' in request.args:
        school = (request.args['school'])

    s1 = school.replace(" ", "_").replace("'", " ").replace(
        "&", "").replace("(", "").replace(")", "")

    with open('./resources/schedules/' + s1 + '.json', 'r') as f:
        schedule = json.loads(f.read())

    return jsonify(schedule)


@app.route("/news")
def news():
    """Look up articles for school"""

    school = request.args.get("school")

    if not school:
        raise RuntimeError("missing school")

    return jsonify(lookup(school)[:8])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
