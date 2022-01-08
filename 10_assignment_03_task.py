import requests
import datetime
from pprint import pprint


def get_stackoverflow_questions():
    date = datetime.datetime.today()
    today = date.strftime('%Y-%m-%d')
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'pagesize': 100,
        'todate': today,
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow',
    }
    response = requests.get(url, params=params)
    questions = response.json()
    len_json = len(questions['items'])
    for counter in range(len_json):
        for key, value in questions['items'][counter].items():
            if key == 'title':
                pprint(value)
        counter += 1


if __name__ == '__main__':
    get_stackoverflow_questions()

