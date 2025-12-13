#!/usr/bin/python3

"""
Module 7-base_geometry
Contains BaseGeometry class with area() and integer_validator()
"""

class BaseGeometry:
    """Base class for geometry shapes"""

    def area(self):
        """Method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
            - name is always a string
            - value must be an integer > 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
