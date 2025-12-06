#!/usr/bin/python3
"""
3-error_code.py: Fetch a URL and display response body,
handle HTTPError and print the error code
"""

from urllib import request, error
import sys


def fetch_url(url):
    """Fetch a URL and print response or error code"""
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    fetch_url(sys.argv[1])
