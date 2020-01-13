#!/usr/bin/python3
"""
sends a search request to the Star Wars API
"""
import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://swapi.co/api/people/?search={}'
                       .format(argv[1]))
    l = req.json().get('results')
    names = []
    for item in l:
        if 'name' in item:
            names.append(item.get('name'))
    print('Number of results: {}'.format(len(names)))
    for name in names:
        print(name)
