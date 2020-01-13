#!/usr/bin/python3
"""
returns the specified header request
"""
import urllib.request as u
import sys

if __name__ == '__main__':
    with u.urlopen(sys.argv[1]) as res:
        print(res.info().get('X-Request-Id'))
