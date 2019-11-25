#!/usr/bin/python3
def complex_delete(d, value):
    keys = [k for k in d if d[k] == value]
    for k in keys:
        d.pop(k)
    return d
