#!/usr/bin/python3
"""a module that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """a recursive function that queries the Reddit API & returns a list
    containing the titles of all hot articles for a <subreddit>

    Parameters:
        subreddit (str): subreddit to queries for.
        hot_list (list): list of hot posts articles.
    """
    user_agent = {'User-Agent': 'hazem0010'}
    query_strings = {
        "after": after,
        "count": count,
        "limit": 100
    }
    url = "https://www.reddit.com/r/{}/hot/".format(subreddit)
    response = requests.get("{}.json".format(url), headers=user_agent,
                            params=query_strings, allow_redirects=False)
    if (response.status_code == 404):
        return None
    res = response.json().get('data')
    after = res.get('after')
    count += res.get('dist')
    for child in res.get('children'):
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
