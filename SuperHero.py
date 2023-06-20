from pprint import pprint
import requests
import json
git 
def super_heroes_all():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    return response.json()

#print(super_heroes_all())

def super_heroes():
    heroes = []
    for i in super_heroes_all():
        if i['name'] == 'Hulk':
            heroes.append({'name': i['name'], 'intelligence': i['powerstats']['intelligence']})
        elif i['name'] == 'Captain America':
            heroes.append({'name': i['name'], 'intelligence': i['powerstats']['intelligence']})
        elif i['name'] == 'Thanos':
            heroes.append({'name': i['name'], 'intelligence': i['powerstats']['intelligence']})
    return heroes


#print(super_heroes())

intelligence_super_hero = 0
name = ''
for intelligence_super in super_heroes():
    if intelligence_super_hero < int(intelligence_super['intelligence']):
        intelligence_super_hero = int(intelligence_super['intelligence'])
        name = intelligence_super['name']

print(f"Самый умный: {name}\n Интелект = {intelligence_super_hero}")