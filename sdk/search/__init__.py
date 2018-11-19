from pprint import pprint

from sdk.request import api_request

BASE_URL = 'search/'


def _reslove_query_params(verticals, query_params, page=1):
    allowed = ['age_groups',
               'ethnic_groups',
               'locations',
               'gender',
               'social_networks',
               'min_followers',
               'max_followers',
               'influencer_city']

    # validate verticals ? or let api fail
    query_params_str = '?&verticals={ids}'.format(ids=','.join(map(str, verticals)))

    if query_params:
        for param in query_params:
            if param in allowed:
                query_params_str += '&{key}={ids}'.format(key=param, ids=','.join(map(str,query_params[param])))

    query_params_str += '&p={p}'.format(p=page)

    return query_params_str


def filters():
    result = api_request('GET', BASE_URL + 'filters/')
    return result.json()


def verticals():
    result = api_request('GET', BASE_URL + 'verticals/')
    return result.json()


def by_text(text, page=1):
    result = api_request('GET', BASE_URL + 'term/?q={q}&p={p}'.format(q=text, p=page))
    return result.json()


# http://127.0.0.1:8001/search/?&social_networks=5&age_groups=3,4&ethnic_groups=2&gender=1&countries=126,27,89&verticals=12,4&min_followers=100000&max_followers=1200000&p=1
def by_params(verticals, page=1, *args, **kwagrgs):
    result = api_request('GET', BASE_URL + _reslove_query_params(verticals, kwagrgs))
    return result.json()
