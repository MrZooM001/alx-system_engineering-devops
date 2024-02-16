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
    url = "https://www.reddit.com/r/{}/about".format(subreddit)
    response = requests.get("{}.json".format(url), headers=user_agent)
    if (response.status_code == 302 or response.status_code == 404):
        return 0
    res = response.json()
    try:
        return res.get('data').get('subscribers')
    except Exception as ex:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
