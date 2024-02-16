#!/usr/bin/python3
"""a module that queries the Reddit API"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API & returns the number
    of all subscribers of the <subreddit>

    Parameters:
        subreddit (str): subreddit to queries for.
    """
    user_agent = {'User-Agent': 'hazem0010'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=user_agent)
    if (response.status_code == 302 or response.status_code == 404):
        return 0
    response = response.json()
    if ('subscribers' in response):
        return response.get('data').get('subscribers')
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
