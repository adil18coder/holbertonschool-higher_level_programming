#!/usr/bin/python3

"""
Module 7-base_geometry
Contains BaseGeometry class with area() and integer_validator()
"""

class BaseGeometry:
    """Base class for geometry objects"""

    def area(self):
        """Raises an exception as it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.
        
        Args:
            name: string (name of the value)
            value: value to validate
        
        Raises:
            TypeError if value is not an integer
            ValueError if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
