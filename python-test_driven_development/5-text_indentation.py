#!/usr/bin/python3

"""
Module description"
"""


def multisplit(s, delims):
    """
    Description of multisplit function
    """
    pos = 0
    for i, c in enumerate(s):
        if c in delims:
            yield s[pos:i+1]
            pos = i + 1
    yield s[pos:]


def text_indentation(text):
    """
    Description of text_indentation function
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    result = list(multisplit(text, '.:?'))
    result = list(map(lambda s: s.strip(), result))
    result = "\n\n".join(result)
    print(result, end="")
