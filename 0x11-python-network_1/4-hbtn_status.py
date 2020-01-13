#!/usr/bin/python3
""" fetches from https://intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    res = requests.get('https://intranet.hbtn.io/status').content
    print("Body response:")
    print("\t- type: {}".format(type(str(res))))
    print("\t- content: {}".format(res.decode('utf-8')))
