#!/usr/bin/python3
"""
10-my_github.py: Fetch your GitHub user ID using Basic Authentication
"""

import requests
import sys


def get_github_id(username, token):
    """Fetch GitHub user ID using provided username and personal access token"""
    url = "https://api.github.com/user"
    response = requests.get(
        url,
        auth=(
            username,
            token
        )
    )
    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
