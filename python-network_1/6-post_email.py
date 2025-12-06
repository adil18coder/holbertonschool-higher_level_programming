#!/usr/bin/python3
"""
6-post_email.py: Send a POST request with an email and display response body
"""

import requests
import sys


def post_email(url, email):
    """Send POST request with email and print response"""
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
