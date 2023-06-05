#!/usr/bin/python3


def multiple_returns(sentence):
    first_char = None
    if sentence is not None:
        first_char = sentence[0]
    length = len(sentence)
    return length, first_char
