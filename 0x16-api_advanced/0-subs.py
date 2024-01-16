#!/usr/bin/python3
""" Querries number of subscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "YourUserAgent"
        }
    response = get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
