# -*- coding: latin-1 -*-

import json
from os import path
from random import randint

import requests

CURRENT_URL = 'http://127.0.0.1:8000/{}'


def nightly_warmup():
    session = requests.Session()
    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']
    session.post(CURRENT_URL.format('api-auth/login/'),
                 data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                 headers={'X-CSRFToken': csrftoken},
                 allow_redirects=False)
    csrftoken = response.cookies['csrftoken']

    language = 'italian'

    response = session.get(CURRENT_URL.format('api-v1/phrases/'),
                           headers={'X-CSRFToken': csrftoken})
    phrases = response.json()

    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': language},
                           headers={'X-CSRFToken': csrftoken})
    language = response.json()
    audio_base = language[0]['audio_base']

    while len(phrases) > 0:
        cur_phrase_pos = randint(0, len(phrases) - 1)
        cur_phrase = phrases[cur_phrase_pos]
        is_listen = randint(0,1)
        if is_listen == 0:
            print("URL: {}{} \n\n".format(audio_base, cur_phrase['audio_id']))
            input("Press any button to see the answer")
            print("Phrase: {} \n\n".format(cur_phrase['english_translation']))
        else:
            print("Phrase: {} \n\n".format(cur_phrase['english_translation']))
            input("Press any button to see the answer")
            print("URL: {}{} \n\n".format(audio_base, cur_phrase['audio_id']))

        was_correct = input("Were you correct? \n1=Yes and 2=No")
        try:
            if was_correct == int(1):
                del(phrases[cur_phrase_pos])
        except:
            print("That's not an option dumbass")


def read_sql():
    session = requests.Session()

    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']

    response = session.post(CURRENT_URL.format('api-auth/login/'),
                           data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                           headers={'X-CSRFToken': csrftoken})
    csrftoken = response.cookies['csrftoken']

    response = session.get(CURRENT_URL.format('api-v1/phrases/'), params={'id': 23}, headers={'X-CSRFToken': csrftoken})
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
                 headers={'X-CSRFToken': csrftoken},
                 allow_redirects=False)

    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': 'italian'},
                           allow_redirects=False)

    response = session.get(CURRENT_URL.format('api-v1/phrases/'))

    phrases = response.json()
    for phrase in phrases:
        session.delete(CURRENT_URL.format('api-v1/phrases/'),
                       data={'id': phrase['id']},
                       headers={'X-CSRFToken': csrftoken},
                       allow_redirects=False)

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
    session = requests.Session()
    language = "Italian"
    english = "The cup"
    italian = u"La Tazza".encode('latin-1')
    url = "https://d7mj4aqfscim2.cloudfront.net/tts/%7Bvoice%7D/sentence/528da82c7ddf412e37643c34c93a1213"
    url = url.split("/")
    url_id = url[len(url)-1]

    response = session.get(CURRENT_URL.format('api-auth/login/'))
    csrftoken = response.cookies['csrftoken']

    session.post(CURRENT_URL.format('api-auth/login/'),
                 data={'username': 'wbeasley', 'password': 'N0ahArthur'},
                 headers={'X-CSRFToken': csrftoken})

    response = session.get(CURRENT_URL.format('api-v1/languages/'),
                           data={'name': language})
    language = response.json()
    r = session.post(CURRENT_URL.format('api-v1/phrases/'),
                     data={'english_translation': english,
                           'foreign_translation': italian,
                           'audio_id': url_id,
                           'language': language[0]['id']},
                     headers={'X-CSRFToken': csrftoken})
    print(r.text)


if __name__ == '__main__':
    nightly_warmup()
