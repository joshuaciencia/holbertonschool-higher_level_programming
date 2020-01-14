#!/usr/bin/python3
"""
get data from SW API with pagination
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    req = requests.get(url)
    print('Number of results: {}'.format(req.json().get('count')))
    while url:
        req = requests.get(url)
        l = req.json().get('results')
        for item in l:
            if 'name' in item:
                film_urls = item.get('films')
                print(item.get('name'))
                for f in film_urls:
                    r = requests.get(f)
                    title = r.json().get('title')
                    print("\t{}".format(title))
        url = req.json().get('next')
