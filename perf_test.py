import string
import time
from threading import Thread

from requests import HTTPError

from examples import *


def single_user_activity():
    # api limit is 100 per minute
    cycles = 0
    erred = False
    while not erred:
        try:
            cycles += 1
            print 'avg_followers'
            avg_followers()

            print 'influencer_a_more_influential_in_the_us_than_influencer_b'
            influencer_a_more_influential_in_the_us_than_influencer_b()

            print 'find_influencers_like_this_guy'

            find_influencers_like_this_guy(name=random.choice(string.letters), pick_random=True)

            print 'vertical_similiarity_score'
            vertical_similiarity_score()

            print 'finished %d cycle of single_user_activity' % cycles
        except HTTPError as e:
            erred = True
            print 'error'
            if e.response.status_code == 429:
                time.sleep(60)
                erred = False


def spin_threads(count):
    for i in range(0, count):
        thread = Thread(target=single_user_activity)
        thread.start()


spin_threads(3)
