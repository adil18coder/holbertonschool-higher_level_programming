#!/usr/bin/python3
"""Module that defines a Student class with serialization and deserialization
capabilities.
"""


class Student:
    """Student class with public attributes, a method to return dictionary
    representation, and a method to reload attributes from a dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.
        If `attrs` is a list of strings, only attributes with names in `attrs`
        are included. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from
        the dictionary `json`.
        """
        for key, value in json.items():
            setattr(self, key, value)
