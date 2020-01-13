#!/usr/bin/python3
"""
returns the specified header request"""
import os
import urllib.request as u


if __name__ == '__main__':
    with u.urlopen(os.sys.argv[1]) as res:
        print(res.info().get('X-Request-Id'))
