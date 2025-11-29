#!/usr/bin/python3
"""Module that returns the JSON representation of an object as a string."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of `my_obj` as a string."""
    return json.dumps(my_obj)
