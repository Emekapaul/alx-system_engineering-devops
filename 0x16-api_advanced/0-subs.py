#!/usr/bin/python3
"""
Module for number_of_subscribers function.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the reddit api and return the total number of subscribers for a given
    subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
                Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
