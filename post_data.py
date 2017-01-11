# -*- coding: utf-8 -*-

from os import path
import json

import requests

CURRENT_URL = 'http://127.0.0.1:8000/{}'
"""
router.register(r'languages', LanguageViewSet)
router.register(r'phrases', PhraseViewSet)
router.register(r'stats', PhraseStatsViewSet)
"""


def update_sql():
    json_path = path.join(path.dirname(__file__), 'italian.json')
    json_path = json_path.replace('\\', '/')
    with open(json_path) as f:
        keys = json.loads(f.read(), encoding="utf-8")

    session = requests.Session()

    r = session.get(CURRENT_URL.format('api-auth/login'), auth=('wbeasley', 'N0ahArthur'))
    session.headers = r.headers
    print(session.headers)
    check = session.post(CURRENT_URL.format('api-v1/languages/'), auth=('wbeasley', 'N0ahArthur'),
                         data={'name': keys['header']['language'], 'audio_base': keys['header']['url_base']})
    import pdb;pdb.set_trace()

    r = session.get(CURRENT_URL.format('api-v1/languages/'), params={'name': 'Italian'})
    print(r)


if __name__ == '__main__':
    update_sql()
