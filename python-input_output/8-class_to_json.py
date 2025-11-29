#!/usr/bin/python3
"""Module that returns the dictionary representation of a class instance
for JSON serialization.
"""


def class_to_json(obj):
    """Returns a dictionary with simple data structure (list, dict, str,
    int, bool) representing `obj`.
    """
    return obj.__dict__.copy()
