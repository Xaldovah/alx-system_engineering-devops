#!/usr/bin/python3
"""
This module provides a function for querying the Reddit API and
printing the titles of the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/requests'}

    response = requests.get(url, headers=headers)

    """Check if the response status code is 200 (OK)"""
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for i, post in enumerate(posts, start=1):
                print(f"{post['data']['title']}")
        else:
            print("None")
    else:
        print("None")
