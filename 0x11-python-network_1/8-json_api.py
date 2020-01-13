#!/usr/bin/python3
"""
send POST req to url with
letter param
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {
        'q': q
    }
    req = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json = req.json()
        if not json:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except Exception as e:
        print("Not a valid JSON")
