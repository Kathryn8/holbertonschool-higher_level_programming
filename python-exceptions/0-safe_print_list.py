#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            counter = counter + 1
    except IndexError:
        print()
        return counter
    else:
        print()
        return counter
