#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(0, len(row)):
            if i == 0:
                print("{}".format(row[i]), end="")
            else:
                print(" {}".format(row[i]), end="")
        print("")
