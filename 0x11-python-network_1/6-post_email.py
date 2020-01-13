#!/usr/bin/python3
"""
displays the email return by a post request
"""
import requests
from sys import argv


if __name__ == '__main__':
    data = {
        'email': argv[2]
    }
    req = requests.post(argv[1], data)
    print(req.content.decode('utf-8'))
