#!/usr/bin/python3
"""
function that lists number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """

    url = "https://www.reddit.com/r/programming/hot.json".format(subreddit)
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
