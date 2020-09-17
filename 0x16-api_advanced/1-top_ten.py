#!/usr/bin/python3
"""
queries the Reddit API
"""
import requests
import sys


def top_ten(subreddit):
    """ Return the first ten post
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    req = requests.get(url, headers=header).json()

    if req.get('error') == 404:
        print("None")
        return

    respon = req.get("data").get("children")

    for iterator, post in enumerate(respon[:10]):
        print(post.get('data').get('title', None))
