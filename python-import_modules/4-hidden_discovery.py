#!/usr/bin/python3
from __pycache__ import hidden_4

if __name__ == "__main__":
    for name in dir(hidden_4):
        if name[0] != "_" and name[1] != "_":
            print(name)
