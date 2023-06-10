#!/usr/bin/python3
def roman_to_int(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    if type(s) is str and s is not None:
        for i, c in enumerate(s):
            try:
                n = n+(-1*d.get(c) if d.get(c) < d.get(s[i+1]) else (d.get(c)))
            except IndexError:
                n = n + d.get(c)
    return n
