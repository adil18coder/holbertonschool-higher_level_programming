#!/usr/bin/python3
"""
8-json_api.py: Send a POST request to search_user API and display results
"""

import requests
import sys


def search_user(letter=""):
    """Send POST request with letter q and print result"""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()
        if response_json:
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
