#!/usr/bin/python3
"""Queries Reddit API and returns the number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Retrieves the number of subscribers in a subreddit"""
    base_url = 'https://www.reddit.com/r/'
    url = f'{base_url}{subreddit}/about.json'

    headers = {'User-Agent': 'MyRedditClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            return 0

        else:
            print(f"Error: {response.status_code}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
