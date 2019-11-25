#!/usr/bin/python3
"""
Module that multiplies two matrices
returns the resulting matrix
"""


def matrix_mul(m_a, m_b):
    """ function that multiplies
    two matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for l in m_a:
        if type(l) is not list:
            raise TypeError("m_a must be a list of lists")
    for l in m_b:
        if type(l) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) is 0 or len(m_a[0]) is 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) is 0 or len(m_b[0]) is 0:
        raise ValueError("m_b can't be empty")
    for l in m_a:
        for e in l:
            if type(e) is not int and type(e) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for l in m_b:
        for e in l:
            if type(e) is not int and type(e) is not float:
                raise TypeError("m_b should contain only integers or floats")
    size = len(m_a[0])
    for l in m_a:
        if len(l) is not size:
            raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    for l in m_b:
        if len(l) is not size:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    col = 0
    n_row = []
    for r in range(len(m_a)):
        row = []
        for c in range(len(m_a)):
            ele = 0
            for k in range(len(m_a[0])):
                ele += m_a[r][k] * m_b[k][c]
            row.append(ele)
        result.append(row)
    return result
