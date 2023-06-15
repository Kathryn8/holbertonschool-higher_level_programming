#!/usr/bin/python3

"""
Module description"
"""


def text_indentation(text):
    """
    Description of text_indentation function
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    print(text.replace("? ", "?\n\n")
          .replace(": ", ":\n\n").replace(". ", ".\n\n"))
