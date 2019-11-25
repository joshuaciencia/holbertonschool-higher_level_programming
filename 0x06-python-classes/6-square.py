#!/usr/bin/python3
class Square:
    """
    Square class representation
    Attributes:
        __size (int): size of square
        position (tuple): coordinates of a square
    """
    def __init__(self, size, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ position getter """
        return self.__position

    @position.setter
    def position(self, position):
        """ position setter """
        if (type(position) != tuple or
                len(position) != 2 or
                type(position[0]) != int or
                type(position[1]) != int or
                position[0] < 0 or
                position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def my_print(self):
        """ print square """
        if self.__size == 0:
            print()
            return
        for it in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
