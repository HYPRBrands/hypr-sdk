import random

from sdk import influencers, search, account


# this makes 3 calls to the api
def avg_followers():
    # get all available verticals
    current_verticals = search.verticals()
    current_filters = search.filters()
    social_netowrks_map = {network_kvp['id']: network_kvp['name'] for network_kvp in current_filters['social_networks']}
    # find the one that means "fashion"
    fashion_vertical = None

    for vertical in current_verticals:
        if vertical['name'].lower() == 'fashion':
            fashion_vertical = vertical['id']
            break

    first_page = search.by_params(verticals=[fashion_vertical])

    followers = {}

    if first_page['total_results'] > 0:
        for influencer_result in first_page['results']:
            for network_stats in influencers.social(public_name=influencer_result['public_name']):
                network_id = network_stats['social_network']['id']
                network_followers = network_stats['stats']['followers']
                if network_id not in followers:
                    followers[network_id] = {'count': 1, 'data': network_followers}
                else:
                    followers[network_id]['count'] += 1
                    followers[network_id]['data'] += network_followers

    avgs = [{social_netowrks_map[network[0]]: network[1]['data'] / network[1]['count']} for network in followers.iteritems()]

    return avgs


# this make 2 calls to the api
def influencer_a_more_influential_in_the_us_than_influencer_b():
    danielle = search.by_text('danielle')['results'][0]
    cosmo = search.by_text('cosmo')['results'][0]

    # reach, engagement and amplification
    score_danielle = reduce(lambda x, y: x + y, danielle['score_stats'].values())
    score_cosmo = reduce(lambda x, y: x + y, cosmo['score_stats'].values())

    return score_danielle > score_cosmo


# this makes 2 calls to the api
# this can be applied to all the stats we have, and used to compare similarity of influencers
def vertical_similiarity_score():
    # get all available verticals
    martin = search.by_text('martin')['results'][0]
    cosmo = search.by_text('cosmo')['results'][0]

    v_map = {v['id']: {'a': v['rank']} for v in martin['vertical_stats']}
    v_map.update({v['id']: {'b': v['rank']} for v in cosmo['vertical_stats']})

    dissimilarity = 0
    for v in v_map.iteritems():
        if 'a' in v[1] and 'b' in v[1]:
            dissimilarity += abs(v[1]['a'] - v[1]['b'])
        else:
            dissimilarity += 1

    similiarity = len(v_map) - dissimilarity

    return similiarity


# this makes 5 calls to the api
def find_influencers_like_this_guy(name='some_influencer', pick_random=False):
    results = search.by_text(name)['results']

    indx = 0
    if pick_random:
        indx = random.randint(0, len(results) - 1)

    some_influencer = results[indx]

    current_filters = search.filters()

    age_groups_map = current_filters['age_groups']
    ethnic_groups_map = current_filters['ethnic_groups']

    verticals = [v['id'] for v in some_influencer['vertical_stats']]
    countries = [g['id'] for g in some_influencer['geo_stats']]

    ages = influencers.age_groups(public_name=some_influencer['public_name'])
    max_age = max(ages, key=ages.get)
    max_age_id = 0
    for age_group in age_groups_map:
        if age_group['name'] == max_age:
            max_age_id = age_group['id']
            break

    ethnic = influencers.ethnic(public_name=some_influencer['public_name'])
    max_ethnic = max(ethnic, key=ethnic.get)
    max_ethnic_id = 0
    for ethnic_group in ethnic_groups_map:
        if ethnic_group['name'] == max_ethnic:
            max_ethnic_id = ethnic_group['id']
            break

    similar_results = search.by_params(verticals=verticals, countries=countries, age_groups=[max_age_id], ethnic_groups=[max_ethnic_id])
    return similar_results


def upload_custom_photos():
    public_name = 'naomi'
    my_dog = open("tony.jpg", "rb")
    account.upload_influencer_pic(public_name, 1, my_dog)

    influencer_settings = account.get_influencer_pic(public_name)
    return influencers['pictures']


def search_and_export():
    # fashion: 12
    # ages 26-32: 3
    # from the US : 248
    # first 5 pages
    results = []
    for page in range(1, 6):
        results = results + search.by_params(verticals=[12], age_groups=[3], countries=[248], page=1)['results']

    from pprint import pprint
    first_2 = results[:2]
    for result in first_2:
        pprint(influencers.full(public_name=result['public_name']))

    guids_to_export = [result['guid'] for result in results[:3]]
    export_result = influencers.export(guids_to_export, template='default')
    print export_result['url']
