#!/usr/bin/python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """Custom class that can be pickled"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object and saves it to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and deserializes a pickled object from a file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
