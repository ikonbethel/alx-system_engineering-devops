#!/usr/bin/python3
'''Module containing subreddit api task'''
import requests


def number_of_subscribers(subreddit):
    '''
    queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
