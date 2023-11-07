#!/usr/bin/python3
"""
This script uses Reddit's API to retrieve
the top post titles for a given subreddit.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieve the top ten post titles for a given subreddit.
    :param subreddit: The name of the subreddit to query.
    :param hot_list: A list to store the top post titles.
    :return: A list containing the top post titles,
        or None if an error occurs.
    """
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
