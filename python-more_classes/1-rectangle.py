#!/usr/bin/python3
"""askl;lefghjkl"""


class Rectangle:
    """asdfghjklhfd"""

    def __init__(self, width=0, height=0):
        """asdfghjkl;"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """asdfkl;"""
        return self.__width

    @width.setter
    def width(self, value):
        """asdfghjkl;"""
        if not isinstance(value ,int):
            raise TypeError("you must include an integer type")
        if value < 0:
            raise ValueError("you must include positive number")
        self._width = value

    @property
    def height(self):
        """asdfghjkl;"""
        return self.__height

    @height.setter
    def height(self, value):
        """asd;lkjhgf"""
        if not isinstance(value ,int):
            raise TypeError("you must include an integer type")
        if value < 0:
            raise ValueError("you must include positive number")
        self._width = value
