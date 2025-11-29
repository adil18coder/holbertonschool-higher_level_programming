#!/usr/bin/python3
"""Module that creates a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates and returns a Python object from a JSON file `filename`."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
