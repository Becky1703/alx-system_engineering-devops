#!/usr/bin/python3
"""Queries a Reddit API and returns the count of the
   hot articles in a subbreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Uses a recursion to retrieve hot articles in Reddit API"""
    base_url = 'https://www.reddit.com/r/'
    url = f'{base_url}{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditCient/1.0'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()

        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None
