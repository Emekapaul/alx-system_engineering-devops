#!/usr/bin/python3
"""
Module containing definition for top_ten function.
"""
import requests


def top_ten(subreddit):
    """Print the titles of top 10 hot post listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
                Safari/537.3'}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print('None')
