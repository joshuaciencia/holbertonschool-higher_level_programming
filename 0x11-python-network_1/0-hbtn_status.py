#!/usr/bin/python3
"""
returns a responde from the intrarnet url
"""
import urllib.request as u


if __name__ == '__main__':
    with u.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
