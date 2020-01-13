#!/usr/bin/python3
""" Displays url response body with error
of http status code
"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get(argv[1])
    code = req.status_code
    if code == 200:
        print(req.content.decode('utf-8'))
    else:
        print(code)
