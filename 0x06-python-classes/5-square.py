#!/usr/bin/python3
class Square:
    """
    Square class representation
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """ square area """
        return self.__size ** 2

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
