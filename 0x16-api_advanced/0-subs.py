#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers (not
active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Use the reddit API to get the number of subscribers
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"

    req = requests.get(url, headers=header)

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
