#!/usr/bin/python3
"""
script retrieves the number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers for the subreddit, or 0 for error
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
