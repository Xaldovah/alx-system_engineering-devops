#!/usr/bin/python3
"""
This module provides a function for querying the Reddit API
to get the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: The number of subscribers if the subreddit is valid, 0 otherwise.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests'}

    response = requests.get(url, headers=headers)

    """Check if the response status code is 200 (OK)."""
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
