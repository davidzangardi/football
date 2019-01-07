import requests
import os
import json

# fetch conferences
c = requests.get('https://api.collegefootballdata.com/conferences')

conferences = c.json()

for conference in conferences:
    a = conference['abbreviation']
    t = requests.get(
        'https://api.collegefootballdata.com/teams?conference=' + a)
    teams = t.json()
    conference['teams'] = teams

with open('./resources/teams/teams.tmp.json', 'w') as g:
    g.write(json.dumps(conferences))
os.rename('./resources/teams/teams.tmp.json',
          './resources/teams/teams.json')
