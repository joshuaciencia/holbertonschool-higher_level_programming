#!/usr/bin/python3
"""
displays header value of url
"""
import requests
from sys import argv


if __name__ == '__main__':
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
