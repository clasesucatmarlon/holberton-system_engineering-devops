#!/usr/bin/python3
""" count word
"""
from collections import Counter, defaultdict
import requests


def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    """ count all words in a subreddit
    """
    agent = "Holberton"
    header = {"User-Agent": agent}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"

    if after:
        url += '?after={}'.format(after)
    try:
        req = requests.get(url, headers=header, allow_redirects=False).json()
        respon = req.get("data").get("children")

        for i in respon:
            cont = Counter(i.get("data").get("title").lower().split(' '))
            for word in word_list:
                if word.lower() in cont:
                    res[word] += cont.get(word.lower())
        after = req.get("data").get("after")

        if after:
            return count_words(subreddit, word_list, res, after)
        f_sort = sorted(res.items(), key=lambda x: x[0])

        for k, v in sorted(f_sort, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))

    except:
        return
