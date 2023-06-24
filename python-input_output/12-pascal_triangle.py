#!/usr/bin/python3
"""Module containing function that produces a pascal's triangle"""


def pascal_triangle(n):
    """Function that return a pascals triangle of size n"""
    if n <= 0:
        return []
    matrix = [[1] for row in range(n)]
    for idx, row in enumerate(matrix):
        for i in range(idx):
            row.append(1)
    for idx, row in enumerate(matrix):
        for idxj, col in enumerate(row):
            if idx > 1 and idxj > 0:
                try:
                    row[idxj] = matrix[idx-1][idxj-1] + matrix[idx-1][idxj]
                except IndexError:
                    row[idxj] = matrix[idx-1][idxj-1] + 0
                except IndexError:
                    row[idxj] = matrix[idx-1][idxj] + 0
    return matrix
