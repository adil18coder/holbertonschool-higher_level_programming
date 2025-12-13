#!/usr/bin/python3

"""
BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        - name is always a string
        - if value is not an integer: raise TypeError
        - if value <= 0: raise ValueError
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
