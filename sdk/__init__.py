API_URL = 'http://127.0.0.1:8001/'
API_KEY = '8c2281945432b1f855d00cb617638532bbb9663d'
#
# API_URL = 'https://api.hyprbrands.com/'
# API_KEY = 'YOUR API KEY'

__all__ = ['influencers', 'perf_scripts', 'search']
from pprint import pprint

import requests

import influencers
import perf_scripts
import search

CHECK_HEALTH_URL = 'checkhealth/'


def ok():
    try:
        result = requests.request('GET', API_URL + CHECK_HEALTH_URL)
        pprint(result)
        if result.status_code == 200:
            return True
    except Exception as e:
        pprint(e)

    return False
