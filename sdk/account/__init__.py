import base64

from sdk.request import api_request


def upload_influencer_pic(public_name, index, img):
    result = api_request('PATCH', 'account/settings/pdf/influencers/{public_name}/pictures/{index}/'.format(public_name=public_name, index=index),
                         files=[('pic', (None, 'data:image/jpeg;base64,' + base64.b64encode(img.read())))])

    return result.json()


def get_influencer_pic(public_name):
    result = api_request('GET', 'account/settings/pdf/influencers/{public_name}/'.format(public_name=public_name))

    return result.json()
