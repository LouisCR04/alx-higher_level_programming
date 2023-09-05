#!/usr/bin/python3
def remove_char_at(str, n):
    l_str = list(str)
    strlen = len(l_str)
    if n < 0 or n > strlen:
        return (str)

    l_str[n] = ""
    str1 = ""
    str1 = str1.join(l_str)
    return (str1)
