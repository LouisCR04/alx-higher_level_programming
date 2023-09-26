#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
-square.py: Defines a Square
"""


class Square:
    """class Square that

    Attributes:
        attr1 (size): Size-Private
        attr2 (area): Area of the square
    """

    def __init__(self, size=0):
        """Init"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Get size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """rints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(self.__size - 1):
                print("#", end="")
            print("#")

    def area(self):
        """Public inst method that return area of square"""
        area = self.__size * self.__size
        return (area)
