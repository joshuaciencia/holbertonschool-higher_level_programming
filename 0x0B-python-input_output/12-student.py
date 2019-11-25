#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = vars(self)
        if attrs is None:
            return d
        new_d = {}
        for k in d:
            if k in attrs:
                new_d[k] = d[k]
        return new_d
