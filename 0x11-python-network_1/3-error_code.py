#!/usr/bin/python3
""" Displays url response body with error
of http status code
"""
import urllib
from sys import argv
import urllib.request as r


if __name__ == '__main__':
    req = r.Request(argv[1])
    try:
        with r.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
