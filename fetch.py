import requests
import os

# fetch conferences
c = requests.get('https://api.collegefootballdata.com/conferences')

with open('/tmp/conferences.tmp.json', 'w') as f:
    f.write(c.text)

os.rename('/tmp/conferences.tmp.json', '/tmp/conferences.json')

conferences = c.json()

# fetch teams
for conference in conferences:
    a = conference['abbreviation']
    t = requests.get(
        'https://api.collegefootballdata.com/teams?conference=' + a)

    with open('/tmp/' + a + '.tmp.json', 'w') as g:
        g.write(t.text)
    os.rename('/tmp/' + a + '.tmp.json', '/tmp/' + a + '.json')

    teams = t.json()

# fetch rosters
    for team in teams:
        s = team['school']
        s1 = s.replace(" ", "%20").replace("&", "%26")
        s2 = s.replace(" ", "_").replace("'", " ").replace(
            "&", "").replace("(", "").replace(")", "")
        r = requests.get(
            'https://api.collegefootballdata.com/roster?team=' + s1)

        with open('/tmp/' + s2 + '.tmp.json', 'w') as h:
            h.write(r.text)
        os.rename('/tmp/' + s2 + '.tmp.json', '/tmp/' + s2 + '.json')
