from __future__ import absolute_import

from pprint import pprint

import sdk


def exceed():
    for i in range(1, 100):
        try:
            result = sdk.influencers.basic('naomi')
            print '%s went fine' % i
        except Exception as e:
            pprint('{0} errored: {1}'.format(i, e))
