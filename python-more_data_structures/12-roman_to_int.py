#!/usr/bin/python3
def roman_to_int(roman_string):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(0, len(roman_string)):
        try:
            if d.get(roman_string[i]) < d.get(roman_string[i + 1]):
                x = -1 * d.get(roman_string[i])
            else:
                x = d.get(roman_string[i])
        except IndexError:
            x = d.get(roman_string[i])
        finally:
            num = num + x
    return num
