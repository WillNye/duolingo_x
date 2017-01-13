# -*- coding: latin-1 -*-

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
    with open(json_path, encoding="latin-1") as f:
        keys = json.loads(f.read())
    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']

    session.post(CURRENT_URL.format('api-auth/login/'),
                 data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                 headers={'X-CSRFToken': csrftoken})

    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': 'italian'})
    language = response.json()
    language = language[0]['id']
    for phrase in keys['translations']:
        english = phrase['english']
        italian = phrase['italian'].encode('latin-1')
        url_id = phrase['audio']
        r = session.post(CURRENT_URL.format('api-v1/phrases/'),
                         data={'english_translation': english,
                               'foreign_translation': italian,
                               'audio_id': url_id,
                               'language': language})
        print(r.text)


def add_phrase():
    print(u"La torta � dolce")
    session = requests.Session()
    language = "Italian"
    english = "The cup"
    italian = u"La Tazza".encode('latin-1')
    url = "https://d7mj4aqfscim2.cloudfront.net/tts/%7Bvoice%7D/sentence/528da82c7ddf412e37643c34c93a1213"
    url = url.split("/")
    url_id = url[len(url)-1]

    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': language})
    language = response.json()
    r = session.post(CURRENT_URL.format('api-v1/phrases/'),
                     data={'english_translation': english,
                           'foreign_translation': italian,
                           'audio_id': url_id,
                           'language': language[0]['id']})
    print(r.text)


def post_test():
    word = u"è".encode('latin-1').decode('latin-1')
    print(word)


if __name__ == '__main__':
    read_sql()
