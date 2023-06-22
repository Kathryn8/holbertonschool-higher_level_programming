#!/usr/bin/python3
"""This module contains the read_file function"""


def read_file(filename=""):
    """Description for read_file function"""
    with open(filename, 'r+', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
