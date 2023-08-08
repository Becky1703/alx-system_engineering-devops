#!/usr/bin/python3
"""Queries Reddit API and prints the titles of the first
   10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """Retrieves top 10 hot posts in a subreddit"""
    base_url = 'https://www.reddit.com/r/'
    url = f'{base_url}{subreddit}/hot.json'

    headers = {'User-Agent': 'MyRedditClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts[:10]:
                print(post['data']['title'])

        elif response.status_code == 404:
            print("None")

        else:
            print(f"Error: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
