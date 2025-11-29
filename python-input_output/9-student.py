#!/usr/bin/python3
"""Module that defines a Student class and returns its dictionary representation
for JSON serialization.
"""


class Student:
    """Student class with public attributes and a method to return dictionary
    representation.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student instance."""
        return self.__dict__.copy()
