#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for i in range(0, len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            my_list.append(my_string[i])
            new_string = ''.join(my_list)
    return new_string
