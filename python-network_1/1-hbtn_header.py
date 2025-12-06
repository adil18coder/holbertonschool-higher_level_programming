#!/usr/bin/python3
"""
1-hbtn_header.py: Fetch a URL and display the value of X-Request-Id in headers
"""

from urllib import request
import sys

if len(sys.argv) < 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Open the URL using a with statement
with request.urlopen(url) as response:
    # Get headers
    headers = response.headers
    # Print X-Request-Id value
    print(headers.get("X-Request-Id"))
