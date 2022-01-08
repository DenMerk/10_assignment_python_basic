import requests
from pprint import pprint

TOKEN = '2619421814940190'
heroes = ['Hulk', 'Captain America', 'Thanos']


def get_request(token, characters):
    intelligence = 0
    most_intelligent_hero = None
    heroes_dict = {}
    for hero in characters:
        url = f'https://superheroapi.com/api/{token}/search/{hero}'
        response = requests.get(url).json()
        hero_intelligence = int(response['results'][0]['powerstats']['intelligence'])
        if hero_intelligence > intelligence:
            intelligence = hero_intelligence
            most_intelligent_hero = response['results'][0]['name']
        heroes_dict[response['results'][0]['name']] = intelligence
    return most_intelligent_hero, heroes_dict


if __name__ == '__main__':
    pprint(get_request(TOKEN, heroes))