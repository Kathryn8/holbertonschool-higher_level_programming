#!/usr/bin/python3
"""Module that contain the function is_same_class"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
