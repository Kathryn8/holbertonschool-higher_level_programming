#!/usr/bin/python3

"""
Module description"
"""


def matrix_divided(matrix, div):
    """
    Description of matrix_divided function
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    row_length_error_message = "Each row of the matrix must have the same size"
    check_lengths = []
    for index, k in enumerate(matrix):
        if type(k) != list:
            raise TypeError(error_msg)
        try:
            if len(k) != len(matrix[index+1]):
                raise TypeError(row_length_error_msg)
        except IndexError:
            pass
        for j in k:
            if type(j) != int and type(j) != float:
                raise TypeError(error_msg)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round(j/div, 2) for j in k] for k in matrix]
    return new
