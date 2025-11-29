#!/usr/bin/python3
"""Module that defines a Student class and returns a filtered dictionary
representation for JSON serialization.
"""


class Student:
    """Student class with public attributes and
 a method to return dictionary
    representation, optionally filtered by attribute names.
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
            # Filter attributes by attrs list
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        # Return all attributes
        return self.__dict__.copy()
