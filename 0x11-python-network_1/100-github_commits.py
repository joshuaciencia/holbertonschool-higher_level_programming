#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))
    l = req.json()
    for i in range(10):
        print("{}: {}".format(l[i].get('sha'),
              l[i].get('author').get('login')))
