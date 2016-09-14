from requests.auth import AuthBase


class ApiAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    API_AUTH_KEY = 'api-key'

    def __init__(self, api_key):
        # setup any auth-related data here
        self.api_key = api_key

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = '{label} {key}'.format(label=self.API_AUTH_KEY, key=self.api_key)
        return r
