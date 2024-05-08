#!/usr/bin/python3
"""Module containing definition for recurse function."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query the reddit api and return a list of hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
                Safari/537.3'}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        list_titles = response.json().get('data').get('children')
        for title in list_titles:
            hot_list.append(title.get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            recurse(subreddit, hot_list, after)
    if hot_list:
        return hot_list
    return None
