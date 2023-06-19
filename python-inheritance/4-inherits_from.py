#!/usr/bin/python3
"""Module that contains the function inherits_from"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ; otherwise
    False.
    """
    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
