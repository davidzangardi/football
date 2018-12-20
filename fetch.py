import os
import json
import requests

# fetch conferences
c = requests.get('https://api.collegefootballdata.com/conferences')

with open('/tmp/conferences.tmp.json', 'w') as f:
    f.write(c.text)

os.rename('/tmp/conferences.tmp.json', '/tmp/conferences.json')

# fetch teams
for conference in json.loads(c):
    a = conference['abbreviation']
    t = requests.get(
        'https://api.collegefootballdata.com/teams?conference=' + a)
    print(json.loads(t))
