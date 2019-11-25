#!/usr/bin/python3
"""
Divides a matrix vy div
params: matrix, div
return: new divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides matrix by div
        returns new divides matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        return []
    for l in matrix:
        if type(l) is not list:
            raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    new_mat = []
    for r in matrix:
        if len(r) != size:
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for c in r:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a \
matrix (list of lists) of integers/floats")
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            num = c / div
            num = round(num, 2)
            row.append(num)
        new_mat.append(row)
    return new_mat
