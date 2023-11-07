#!/usr/bin/python3
"""
This module provides a recursive function that queries the Reddit API,
parses the titles of hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces)
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively fetch and count the keywords in the titles of hot articles
    for a given subreddit.

    :param subreddit: The name of the subreddit.
    :param word_list: A list of keywords to count.
    :param after: A parameter for pagination (default is None).
    :param word_count: A dictionary to store the counts of keywords
    (default is an empty dictionary).
    :return: None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'Python/requests'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            print_result(word_count)
            return

        for post in posts:
            title = post['data']['title']
            count_keywords(title, word_list, word_count)

        after = data['data']['after']
        count_words(subreddit, word_list, after, word_count)
    else:
        print_result(word_count)


def count_keywords(title, word_list, word_count):
    """
    Count keywords in a title and update the word_count dictionary.

    :param title: The title of a Reddit post.
    :param word_list: A list of keywords to count.
    :param word_count: A dictionary to store the counts of keywords.
    :return: None.
    """
    for keyword in word_list:
        if keyword.lower() in title.lower():
            word_count[keyword.lower()] = word_count.get(
                    keyword.lower(), 0) + 1


def print_result(word_count):
    """
    Print the sorted results of keyword counts.

    :param word_count: A dictionary containing keyword counts.
    :return: None.
    """
    for word in sorted(word_count, key=lambda x: (-word_count[x], x)):
        print(f"{word}: {word_count[word]}")
