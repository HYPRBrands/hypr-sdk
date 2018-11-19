from sdk.request import api_request

BASE_PATH = 'influencers/'
INFLUENCER_BY_ID = BASE_PATH + 'id/{id}'
INFLUENCER_BY_GUID = BASE_PATH + 'guid/{guid}/'
INFLUENCER_BY_NAME = BASE_PATH + 'name/{name}/'


def _url_resolver(public_name, guid):
    _url = ''

    if public_name:
        _url = INFLUENCER_BY_NAME.format(name=public_name)
    elif guid:
        _url = INFLUENCER_BY_GUID.format(guid=guid)
    else:
        raise ValueError('No identifier provided')

    return _url


def basic(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'basic/')

    return result.json()


def verticals(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'verticals/')

    return result.json()


def social(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'social/')

    return result.json()


def geo(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'geo/')

    return result.json()


def age_groups(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'ageGroups/')

    return result.json()


def ethnic(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'ethnic/')

    return result.json()


def score(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'score/')

    return result.json()


def gender(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid) + 'gender/')

    return result.json()


def full(public_name=None, guid=None):
    result = api_request('GET', _url_resolver(public_name, guid))

    return result.json()


def export(guids, template='default'):
    result = api_request('POST', BASE_PATH + 'export/pdf/?template={template}'.format(template=template), json={'influencers': guids})

    return result.json()
