import requests
import json


def _url(path):
    return 'https://api.collegefootballdata.com/' + path


def get_conferences():
    return requests.get(_url('/conferences'))


def get_teams(abbrev):
    t = requests.get(_url('teams?conference=' + abbrev))
    if t.status_code != 200:
        # raise ApiError('cannot create task: {}'.format(t.status_code))
        pass
    return t


def get_roster(teamname):
    return requests.get(_url('roster?team=' + teamname))
