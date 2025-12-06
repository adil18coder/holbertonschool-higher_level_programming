#!/usr/bin/python3
"""
7-error_code.py: Fetch a URL and display response body,
handle HTTP status codes >= 400
"""

import requests
import sys


def fetch_url(url):
    """Fetch a URL and print response or error code if >=400"""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url(sys.argv[1])
