#!/bin/python3

import requests, json, datetime, os

d = int(datetime.datetime.now().strftime('%s'))-80

r = requests.get('https://aoe2.net/api/matches', params={
  'game': 'aoe2de',
  'start': 0,
  'count': 10000,
  'since': d,
})

names = {}

try:
  with open('names.json') as json_file:
    names = json.load(json_file)
  n1 = len(names)
except:
  n1 = 0

for game in r.json():
  for player in game['players']:
    if player['profile_id']:
      names[str(player['profile_id'])] = {'name': player['name'], 'ts': game['started']}
      # ~ print(player['profile_id'], player['name'])


with open('names.json-tmp', 'w') as outfile:
  json.dump(names, outfile)
n2 = len(names)
print('Read %d, wrote %d names (%d new from %d games) to file' % (n1, n2, n2-n1, len(r.json())))
os.rename('names.json-tmp', 'names.json')
