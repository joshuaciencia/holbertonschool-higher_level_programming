#!/usr/bin/python3
"""
Module for Base class
"""
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ ctor for Base Class """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(l):
        """ converts list to json string """
        if l is None or len(l) == 0:
            return "[]"
        return json.dumps(l)

    @classmethod
    def save_to_file(cls, l):
        """ save list of objs to a json file """
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if l is None:
                f.write(Base.to_json_string([]))
            else:
                li = []
                for obj in l:
                    li.append(obj.to_dictionary())
                f.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_s):
        """ converts json string to python object """
        if json_s is None or not json_s:
            return []
        else:
            return json.loads(json_s)

    @classmethod
    def create(cls, **dictionary):
        """ create a Base inheritanced object based
        on dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        name = cls.__name__
        if name == "Rectangle":
            dummy = Rectangle(3, 8)
        else:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ loads objects from a json file """
        from os.path import exists
        filename = cls.__name__ + ".json"
        if not exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            s = f.read()
            instances = []
            dics = Base.from_json_string(s)
            for elem in dics:
                instances.append(cls.create(**elem))
            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves objects to a csv file """
        import csv
        name = cls.__name__ + ".csv"
        f = open(name, "w", encoding="utf-8")
        writer = csv.writer(f)
        for obj in list_objs:
            dic = obj.to_dictionary()
            values = list(dic.values())
            keys = list(dic.keys())
            csv_dic = []
            csv_dic.append(keys)
            csv_dic.append(values)
            writer.writerow(keys)
            writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """ loads objects from a csv file """
        import csv
        from os.path import exists
        name = cls.__name__ + ".csv"
        if not exists(name):
            return []
        f = open(name, "r", encoding="utf-8")
        reader = csv.reader(f)
        objs = []
        rect = True if cls.__name__ == "Rectangle" else False

        for row in reader:
            dic = {}
            keys = reader[row]
            values = row[row + 1]
            for i in range(len(keys)):
                dic[keys[i]] = values[i]
            objs.append(cls.create(**dic))
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draws rect and square objects to a canvas """
        import turtle
        turt = turtle.Turtle()
