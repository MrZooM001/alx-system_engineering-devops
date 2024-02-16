#!/usr/bin/python3
"""a module that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, match_list=[], after=None):
    """a recursive function that queries the Reddit API & returns a list
    containing the titles of all hot articles for a <subreddit>

    Parameters:
        subreddit (str): subreddit to queries for.
        hot_list (list): list of hot posts articles.
    """
    if subreddit is None or subreddit == "?":
        return None
    if after is None:
        word_list = [word.lower() for word in word_list]
    user_agent = {'User-Agent': 'hazem0010'}
    url = "https://www.reddit.com/r/{}/hot/".format(subreddit)
    response = requests.get("{}.json?after={}".format(url, after),
                            headers=user_agent)

    if response.status_code == 200:
        res = response.json().get('data')
        next = res.get('after')
        posts = res.get('children')
        for post in posts:
            title = post.get('data').get('title').lower()
            for word in title.split(" "):
                if word in word_list:
                    match_list.append(word)

        if next is not None:
            count_words(subreddit, word_list, match_list, next)
        else:
            result = {}
            for word in match_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(),
                                     key=lambda element: element[1],
                                     reverse=True):
                print("{}: {}".format(key, value))
    else:
        return
