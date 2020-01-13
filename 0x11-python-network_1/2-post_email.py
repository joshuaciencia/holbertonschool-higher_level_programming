#!/usr/bin/python3
"""
displays the email return by a post request
"""
import urllib.parse as p
import urllib.request as r
from sys import argv


if __name__ == '__main__':
    values = {
        'email': argv[2]
    }
    data = p.urlencode(values)
    data = data.encode('ascii')
    req = r.Request(argv[1], data)
    with r.urlopen(req) as res:
        body = res.read().decode('utf-8')
        print(body)
