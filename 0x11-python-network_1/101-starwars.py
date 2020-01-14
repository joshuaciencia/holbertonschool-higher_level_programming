#!/usr/bin/python3
"""
get data from SW API with pagination
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    names = []
    while url:
        req = requests.get(url)
        l = req.json().get('results')
        for item in l:
            if 'name' in item:
                names.append(item.get('name'))
        url = req.json().get('next')
    print('Number of results: {}'.format(len(names)))
    for name in names:
        print(name)
