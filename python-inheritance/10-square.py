#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with size."""
        self.integer_validator("size", size)
        self.__size = size
        # Call parent Rectangle __init__ with width and height equal to size
        super().__init__(size, size)
