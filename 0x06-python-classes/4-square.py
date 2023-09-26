#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
4-square.py: Defines a Square
"""


class Square:
    """class Square

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

    def area(self):
        """Public inst method that return area of square"""
        area = self.__size * self.__size
        return (area)

    
