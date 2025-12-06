#!/usr/bin/python3
"""
2-post_email.py: Send a POST request with an email and display response body
"""

from urllib import request, parse
import sys

url = sys.argv[1]
email = sys.argv[2]

# Prepare the POST data
data = parse.urlencode({'email': email}).encode('utf-8')

# Create a POST request
req = request.Request(url, data=data, method='POST')

# Send the request using with statement
with request.urlopen(req) as response:
    body = response.read()
    print(body.decode('utf-8'))
