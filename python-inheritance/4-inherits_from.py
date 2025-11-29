#!/usr/bin/python3
"""Function that returns True if obj is an instance of a class
that inherited from a_class."""


def inherits_from(obj, a_class):
    """Return True if obj is a subclass instance of a_class, else False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
