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
        """
        if idx % 2 != 0: #odd idx
            row.append(1)
        if idx % 2 == 0 and idx > 0: #even idx
            row.append(1)"""
    for idx, row in enumerate(matrix):
        for idxj, col in enumerate(row):
            #print("col is: {} / idx: {}".format(col, idx))
#            if idx > idxj:
            if idx > 0:
                try:
                    col = matrix[idx-1][idxj-1] + matrix[idx-1][idxj]
                except IndexError:
                    col = matrix[idx-1][idxj-1] + 0
                except IndexError:
                    col = matrix[idx-1][idxj] + 0
                    """
                    if idx > 1:
                    row[1] = matrix[idx-1][0] + matrix[idx-1][1]
                    if idx > 2:
                    row[2] = matrix[idx-1][1] + matrix[idx-1][2]
                    if idx > 3:
                    row[3] = matrix[idx-1][2] + matrix[idx-1][3]"""
    return matrix
