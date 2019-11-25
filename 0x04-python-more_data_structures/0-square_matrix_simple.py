#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for l in matrix:
        m.append(list(map(lambda x: x * x, l)))
    return m
