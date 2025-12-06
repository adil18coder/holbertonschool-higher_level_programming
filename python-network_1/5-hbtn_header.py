#!/usr/bin/python3
"""
5-hbtn_header.py: Fetch a URL and display the value of X-Request-Id in headers
"""

import requests
import sys

url = sys.argv[1]

# Send GET request
response = requests.get(url)

# Print X-Request-Id header value
print(response.headers.get("X-Request-Id"))
