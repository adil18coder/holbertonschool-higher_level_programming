#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        # Validate width and height using BaseGeometry method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Private attributes
        self.__width = width
        self.__height = height
