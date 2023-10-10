#!/usr/bin/python3
""" How many Subs? """
from requests import get 


def number_of_subscribers(subreddit):
    """ Queries the Reddit API
        
        Returns the total number of subscribers in a given subreddit
    """
    header = {'User-Agent': 'Google Chrome Version 117.0.5938.150'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=header, allow_redirects=False)
    reddits = response.json()

     try:
        return reddits.get('data').get('subscribers')
    except Exception:
        return 0
