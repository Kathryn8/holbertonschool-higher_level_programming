#!/usr/bin/python3


def multiple_returns(sentence):
    first_char = None
    length = len(sentence)
    if sentence is not None and length > 0:
        first_char = sentence[0]
    return length, first_char
