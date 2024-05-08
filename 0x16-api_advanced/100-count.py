#!/usr/bin/python3
"""Module containing definition for count_words function."""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively query the reddit api and return a list of hot posts."""
    url = "https://www.reddit.com/r{}/hot.json".format(subreddit)
    params = {'after': after}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 \
                Safari/537.3'}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return

    for list_titles in res.json().get('data').get('children'):
        title = list_titles.get('data').get('title').lower()
        for word in word_list:
            if word.lower() in title:
                word_count[word] = word_count.get(word, 0)
                + title.count(word.lower())
    after = res.json().get('data').get('after')
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        sorted_counts = sorted(word_count.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print("{}: {}".format(word.lower(), count))
