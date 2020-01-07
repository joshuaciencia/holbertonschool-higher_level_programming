#!/usr/bin/python3
"""
finds a peak in a unsorted list of
integers
"""


def find_peak(l):
    """ finds the pick in an unsorted list
    of integers """
    s = len(l)
    if s is 1:
        return l[0]
    for i in range(s):
        if i == 0 and l[0] >= l[1]:
            return l[0]
        elif i == s - 1 and l[s - 1] >= l[s - 2]:
            return l[s - 1]
        elif l[i] >= l[i - 1] and l[i] >= l[i + 1]:
            return l[i]
