#!/usr/bin/python3
"""Function that returns True if obj is an instance of a_class or inherits from it."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass, else False."""
    return isinstance(obj, a_class)
