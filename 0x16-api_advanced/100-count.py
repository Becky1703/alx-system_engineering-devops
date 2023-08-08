#!/usr/bin/python3
"""Queries the reddit API"""
import requests
from sys import argv


def recurse_count(subreddit, hot_list=[], after=None):
    """Function queries reddit API using recursion"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    payload = {"after": after, "limit": 100}
    headers = {"User-Agent": "Python/requests"}

    try:
        req = requests.get(url, headers=headers, params=payload,
                           allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            after = data.get("data")["after"]
            for post in data.get("data")["children"]:
                hot_list.append(post.get('data')['title'])
            if after:
                return recurse_count(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.JSONDecodeError:
        pass


def count_words(subreddit, word_list):
    """Queries the Reddit API and sorts a list of words by occurences"""
    word_dict = {}

    all_titles = recurse_count(subreddit)
    word_list = [w.lower() for w in word_list]

    if all_titles:
        for word in word_list:
            count = 0
            for title in all_titles:
                title = [w.lower() for w in title.split()]

                if word in title:
                    for w in title:
                        if word == w:
                            count += 1

            if count:
                if word_dict.get(word):
                    count += word_dict[word]
                word_dict[word] = count
        sorted_dict = dict(sorted(word_dict.items(),
                           key=lambda item: item[1], reverse=True))
        for k, v in sorted_dict.items():
            print("{}: {:d}".format(k, v))
