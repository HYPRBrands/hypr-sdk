import datetime

import requests
from requests import HTTPError

from auth import ApiAuth
from sdk import API_KEY, API_URL


def api_request(method, path, *args, **kwargs):
    time_start = datetime.datetime.now()
    resp = requests.request(method or 'GET', API_URL + path, auth=ApiAuth(api_key=API_KEY), *args, **kwargs)
    took = datetime.datetime.now() - time_start
    print 'request took %s sec.' % took.total_seconds()
    if resp.status_code != 200:
        if resp.status_code == 429:
            http_error_msg = 'Too many requests (429), retry after %s' % resp.headers['Retry-After']
            raise HTTPError(http_error_msg, response=resp)

        else:
            resp.raise_for_status()

    return resp
