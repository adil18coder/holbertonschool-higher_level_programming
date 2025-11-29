#!/usr/bin/python3
"""Basic Serialization and Deserialization Module"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to JSON and saves it to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it into a Python dictionary"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
