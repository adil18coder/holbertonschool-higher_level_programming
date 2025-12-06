#!/usr/bin/python3
"""
5-hbtn_header.py: Fetch a URL and display the value of X-Request-Id in headers
"""

import requests
import sys


def get_x_request_id(url):
    """Fetch a URL and print the X-Request-Id header value"""
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    get_x_request_id(sys.argv[1])
