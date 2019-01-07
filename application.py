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


@app.route("/teams")
def teams():
    with open('./resources/teams/teams.json', 'r') as e:
        teams = json.loads(e.read())
    return jsonify(teams)


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


@app.route("/Roster", methods=['GET'])
def Rosters():

    if 'school' in request.args:
        school = (request.args['school'])
    else:
        school = None

    s1 = school.replace(" ", "_").replace("'", " ").replace(
        "&", "").replace("(", "").replace(")", "")

    with open('./resources/rosters/' + s1 + '.json', 'r') as h:
        roster = json.loads(h.read())

    return jsonify(roster)


@app.route("/Schedule", methods=['GET'])
def Schedule():

    if 'school' in request.args:
        school = (request.args['school'])

    s1 = school.replace(" ", "_").replace("'", " ").replace(
        "&", "").replace("(", "").replace(")", "")

    with open('./resources/schedules/' + s1 + '.json', 'r') as i:
        schedule = json.loads(i.read())

    return jsonify(schedule)


@app.route("/News")
def News():
    """Look up articles for school"""

    school = request.args.get("school")

    if not school:
        raise RuntimeError("missing school")

    return jsonify(lookup(school)[:8])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
