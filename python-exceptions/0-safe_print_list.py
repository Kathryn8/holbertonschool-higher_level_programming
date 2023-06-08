#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    if x < 1:
        return 0
    if my_list is None:
        return 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
        print()
        return i + 1
    except IndexError:
        print()
        return i
