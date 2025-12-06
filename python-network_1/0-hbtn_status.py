#!/usr/bin/python3
"""
0-hbtn_status.py: Fetch https://intranet.hbtn.io/status
using urllib and display the body response
"""

from urllib import request

url = "https://intranet.hbtn.io/status"

# Open the URL using a with statement
with request.urlopen(url) as response:
    content = response.read()  # content as bytes
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
