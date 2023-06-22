#!/usr/bin/python3
"""This module contains the write_file function"""


def write_file(filename="", text=""):
    """Description for write_file function"""
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
