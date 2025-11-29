#!/usr/bin/python3
"""Module that writes a Python object to a text file as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object `my_obj` to a text file `filename` in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
