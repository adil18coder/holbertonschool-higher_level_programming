#!/usr/bin/python3
"""
4-hbtn_status.py: Fetch https://intranet.hbtn.io/status using requests
and display the body of the response
"""

import requests

url = "https://intranet.hbtn.io/status"

# Send GET request
response = requests.get(url)

# Body content as string
content = response.text

# Print response info
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
