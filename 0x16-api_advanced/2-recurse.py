#!/usr/bin/python3
""" Hot topics? """
from requests import get


def number_of_subscribers(subreddit):
    """ Recursive function that queries the Reddit API

        and returns a list containing the titles of all hot articles
        for a given subreddit.
    """
    header = {'User-Agent': 'Google Chrome Version 117.0.5938.150'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=header, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except:
        print(None)
        return 0
