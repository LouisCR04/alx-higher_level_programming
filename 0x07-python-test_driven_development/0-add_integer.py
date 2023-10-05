#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" This module is create with the add function
The objetive of this function is to add numbers
"""


def add_integer(a, b=98):

    """This is a function that adds 2 integers.
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float

    Args:
        a (int): The first parameter.
        b (int): The second parameter, loaded to 98

    Returns:
         An integer: the addition of a and b

    Raises:
        TypeError: if a or b don't be integers
            exception with the message a must be an integer
            or b must be an integer

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if a != a:
        raise TypeError('a must be an integer')
    if b != b:
        raise TypeError('a must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
