#!/usr/bin/python3
"""
This module provides a recursive function for querying the Reddit API and
accumulating the titles of hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetch and accumulate the titles of hot articles for a given
    subreddit.

    :param subreddit: The name of the subreddit.
    :param hot_list: A list to store the titles (default is an empty list).
    :param after: A parameter for pagination (default is None).
    :return: A list containing the titles of hot articles,
    or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {'User-Agent': 'Python/requests'}
    query_str = {'after': after, 'limit': '100'}

    response = requests.get(url, headers=headers, params=query_str,
            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        hot_posts = response.get('data').get('children')
        after = response.get('data').get('after')

        for post in hot_posts:
            hot_list.append(post.get('data').get('title'))

        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    return None
