#!/usr/bin/python3
"""Number of subscribers for a given subreddit"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'api_advanced-project'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
