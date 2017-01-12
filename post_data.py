# -*- coding: utf-8 -*-

from os import path
import json

import requests

CURRENT_URL = 'http://127.0.0.1:8000/{}'


def read_sql():
    session = requests.Session()

    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']

    response = session.post(CURRENT_URL.format('api-auth/login/'),
                           data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                           headers={'X-CSRFToken': csrftoken})
    response = session.get(CURRENT_URL.format('api-v1/phrases/'), params={'id': 23})
    test = response.json()
    print(test)
    print(response.url)


def update_sql():
    session = requests.Session()
    json_path = path.join(path.dirname(__file__), 'italian.json')
    json_path = json_path.replace('\\', '/')
    with open(json_path) as f:
        keys = json.loads(f.read(), encoding="utf-8")

    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']

    response = session.post(CURRENT_URL.format('api-auth/login/'),
                           data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                           headers={'X-CSRFToken': csrftoken})
    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': keys['header']['language']})
    language = response.json()
    for phrase in keys['translations']:
        print(phrase['english'])
        print(phrase['italian'])
        print(phrase['audio'])
        r = session.post(CURRENT_URL.format('api-v1/phrases/'),
                         data={'english_translation': phrase['english'],
                               'foreign_translation': phrase['italian'],
                               'audio_id': phrase['audio'],
                               'language': language[0]['id']})
        print(r.text)

if __name__ == '__main__':
    read_sql()
