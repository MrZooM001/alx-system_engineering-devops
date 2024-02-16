#!/usr/bin/python3
"""a module that queries the Reddit API"""
import requests
from sys import argv


def top_ten(subreddit):
    """a function that queries the Reddit API
    & returns the top 10 posts of the <subreddit>

    Parameters:
        subreddit (str): subreddit to queries for.
    """
    user_agent = {'User-Agent': 'hazem0010'}
    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    response = requests.get("{}.json?limit=10".format(url), headers=user_agent)
    if (response.status_code == 302 or response.status_code == 404):
        return None
    res = response.json()
    try:
        for post in res.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception as ex:
        return None
