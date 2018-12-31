import requests
import os

# fetch conferences
c = requests.get('https://api.collegefootballdata.com/conferences')

with open('./resources/teams/conferences.tmp.json', 'w') as f:
    f.write(c.text)

os.rename('./resources/teams/conferences.tmp.json',
          './resources/teams/conferences.json')

conferences = c.json()

# fetch teams
for conference in conferences:
    a = conference['abbreviation']
    t = requests.get(
        'https://api.collegefootballdata.com/teams?conference=' + a)

    with open('./resources/teams/' + a + '.tmp.json', 'w') as g:
        g.write(t.text)
    os.rename('./resources/teams/' + a + '.tmp.json',
              './resources/teams/' + a + '.json')

    teams = t.json()

# fetch rosters
    for team in teams:
        s = team['school']
        s1 = s.replace(" ", "%20").replace("&", "%26")
        s2 = s.replace(" ", "_").replace("'", " ").replace(
            "&", "").replace("(", "").replace(")", "")
        r = requests.get(
            'https://api.collegefootballdata.com/roster?team=' + s1)

        with open('./resources/rosters/' + s2 + '.tmp.json', 'w') as h:
            h.write(r.text)
        os.rename('./resources/rosters/' + s2 + '.tmp.json',
                  './resources/rosters/' + s2 + '.json')

        # fetch schedules
        schedule = requests.get(
            'https://api.collegefootballdata.com/games?year=2018&seasonType=regular&team=' + s1)

        with open('./resources/schedules/' + s2 + '.tmp.json', 'w') as i:
            i.write(schedule.text)
        os.rename('./resources/schedules/' + s2 + '.tmp.json',
                  './resources/schedules/' + s2 + '.json')
