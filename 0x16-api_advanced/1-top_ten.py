#!/usr/bin/python3
"""prints top ten posts for reddit"""

from requests import get


def top_ten(subreddit):
    """queries the API
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "YourUserAgent"
        }
    response = get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("No posts found.")
    else:
        print(None)
