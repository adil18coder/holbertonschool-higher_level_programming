#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"
    auth = (username, token)
    response = requests.get(url, auth=auth)

    try:
        print(response.json().get("id"))
    except Exception:
        print(None)
