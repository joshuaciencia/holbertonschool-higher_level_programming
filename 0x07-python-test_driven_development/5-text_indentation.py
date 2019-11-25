#!/usr/bin/python3
"""
This module cuts line with
'., ?, ;' delimeters
"""


def text_indentation(text):
    """Cuts lines with
    : ? . delimeters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = True
    for i in range(len(text)):
        c = text[i]
        if flag and c is " ":
            continue
        print(text[i], end="")
        if text[i] in (".", "?", ":"):
            flag = True
            print()
            print()
        else:
            flag = False
