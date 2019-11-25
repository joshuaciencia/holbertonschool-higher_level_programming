#!/usr/bin/python3
"""Module that reads a file
"""


def read_file(filename=""):
    """ reads files and returns its content"""
    with open(filename, 'r',  encoding="utf-8") as f:
        print(f.read(), end="")
