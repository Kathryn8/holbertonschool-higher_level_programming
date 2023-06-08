#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    if x < 1:
        return 0
    if my_list is None:
        return 0
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter = counter + 1
        except (ValueError, TypeError):
            continue
    print()
    return counter
