#!/usr/bin/python3
"""
Module representation of a rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        s = ""
        for r in range(self.__height):
            for c in range(self.__width):
                s += "#"
            if r != self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
