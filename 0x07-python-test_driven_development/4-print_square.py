#!/usr/bin/python3
"""
Module that prints a square
according to the size passed
"""


def print_square(size):
    """ Prints square
    according to size
    """
    if type(size) is not int or type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print()
