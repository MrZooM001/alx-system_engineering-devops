#!/usr/bin/python3
"""a module that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """a recursive function that queries the Reddit API & returns a list
    containing the titles of all hot articles for a <subreddit>

    Parameters:
        subreddit (str): subreddit to queries for.
        hot_list (list): list of hot posts articles.
    """
    if subreddit is None or subreddit == "?":
        return None
    if after is None:
        return hot_list
    user_agent = {'User-Agent': 'hazem0010'}
    query_strings = {
        "after": after,
        "limit": 100
    }
    url = "https://www.reddit.com/r/{}/hot/".format(subreddit)
    response = requests.get("{}.json".format(url), headers=user_agent,
                            params=query_strings, allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json().get('data')
    after = res.get('after')
    for child in res.get('children'):
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        print('*')
        return recurse(subreddit, hot_list, after)
    return hot_list
