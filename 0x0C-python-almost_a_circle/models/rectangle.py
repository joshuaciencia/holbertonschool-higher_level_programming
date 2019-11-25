#!/usr/bin/python3
"""
Module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ ctor of Rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, w):
        """ width setter """
        if type(w) != int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @height.setter
    def height(self, h):
        """ height setter """
        if type(h) != int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ get are of rectangle """
        return self.__width * self.__height

    def display(self):
        """ show rectangle """
        print("\n" * self.__y, end="")

        for h in range(self.__height):
            print(" " * self.__x, end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ display rectangle info """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x,
                        self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ updates rect attributes """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """ convert to dictionary """
        dic = vars(self)
        new_dic = {}
        for k, v in dic.items():
            k = k.replace("_Rectangle__", "")
            new_dic[k] = v
        return new_dic
