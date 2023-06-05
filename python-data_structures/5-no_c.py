#!/usr/bin/python3


def no_c(my_string):
    my_list = []
    my_list[:0] = my_string
    new_string = ''
    for i in range(0, len(my_list)):
        if my_list[i] != 'c' and my_list[i] != 'C':
            new_string = new_string + ''.join(my_list[i])
    return new_string
