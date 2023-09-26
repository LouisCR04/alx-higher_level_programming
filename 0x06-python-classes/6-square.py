#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
6-square.py: Defines a Square
"""


class Square:
    """class Square that

    Attributes:
        attr1 (size): Size-Private
        attr2 (area): Area of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Init"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.position = position

    def area(self):
        """Public inst method that return area of square"""
        area = self.__size * self.__size
        return (area)

    @property
    def size(self):
        """Get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of square"""
        if not instance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Get current position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets square position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Print the square with the # xter"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
