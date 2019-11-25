#!/usr/bin/python3
"""
adds two integers.
params: a, b
return: a + b
"""


def add_integer(a, b=98):
    """ Adds two integers.
        returns the result of the addition
    """

    a = int(a) if type(a) is float else a
    b = int(b) if type(b) is float else b

    if a is None or type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
