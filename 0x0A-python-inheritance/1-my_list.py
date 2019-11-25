#!/usr/bin/python3
"""
Module representation of a list class
"""


class MyList(list):
    def print_sorted(self):
        """
        prints the list in sorted way, ascending order
        """
        l = self[:]
        l.sort()
        print(l)
