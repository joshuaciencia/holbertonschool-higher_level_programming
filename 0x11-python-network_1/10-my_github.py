#!/usr/bin/python3
"""
authenticates into github
"""
from requests.auth import HTTPBasicAuth
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get('https://api.github.com/user',
                       auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get('id'))
