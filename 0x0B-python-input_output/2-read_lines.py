#!/usr/bin/python3
"""
Module that read n lines from a file
"""
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ read nb_lines lines from line """
    lines = number_of_lines(filename)
    lines_to_read = 0
    if nb_lines <= 0 or nb_lines >= lines:
        lines_to_read = lines
    else:
        lines_to_read = nb_lines

    with open(filename, "r", encoding="utf-8") as f:
        c = 0
        for l in f:
            print(l, end="")
            c += 1
            if c >= lines_to_read:
                break
