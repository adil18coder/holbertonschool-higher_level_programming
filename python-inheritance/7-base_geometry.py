#!/usr/bin/python3

"""BaseGeometry class with area method and integer validator."""


class BaseGeometry:
    """A base class for geometry objects."""

    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.

        Args:
            name (str): The name of the value (always a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
