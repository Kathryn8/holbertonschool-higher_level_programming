#!/usr/bin/python3
"""This module contains the write_file function"""


def append_write(filename="", text=""):
    """Appends a string to end of textfile"""
    with open(filename, 'a', encoding='utf-8') as open_file:
        num_char = open_file.write(text)
        return num_char
