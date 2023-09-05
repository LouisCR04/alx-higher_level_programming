#!/usr/bin/python3
"""
uppercase - Prints a string in upper case
str: String to convert
return void
"""


def uppercase(str):
    l_str = list(str)
    for i in range(len(l_str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            l_str[i] = chr(ord(l_str[i]) - 32)

        print("{}".format(l_str[i]), end="")
    print("")
