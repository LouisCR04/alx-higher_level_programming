#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
2-square.py: Class Square that defines a square
"""


class Square:
    """class Square that defines a square

    Attributes:
        attr1 (_Square__size): Private inst attr of size

    """


def __init__(self, size=0):
    """Init with def size 0"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >=0")

    self.__size = size
