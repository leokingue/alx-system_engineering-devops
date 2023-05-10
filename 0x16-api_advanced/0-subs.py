#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Args:
        subreddit : subreddit name
    return :
        number of suscribers to the subreddit
        or 0 itsubreddit requested is invalid"""
    headers = {"User-Agent": 'leokingue'}
    base_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("suscribers"))
    return 0
