#!/usr/bin/python3
"""
Module for Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ square class ctor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ display square info """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates attributes """
        try:
            self.id = args[0]
            self.width = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "size":
                self.width = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """ to dictionary """
        dic = vars(self)
        new_dic = {}
        for k, v in dic.items():
            k = k.replace("_Rectangle__", "")
            if k == "width":
                k = "size"
            elif k == "height":
                continue
            new_dic[k] = v
        return new_dic
