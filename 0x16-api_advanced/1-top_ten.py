#!/usr/bin/python3
""" How many Subs? """
from requests import get


def top_ten(subreddit):
    """ Queries the Reddit API

        Prints the titles of the first 10 hot posts
        listed for a given subreddit
    """
    header = {'User-Agent': 'Google Chrome Version 117.0.5938.150'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=header, params=params, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except:
        print('None')
