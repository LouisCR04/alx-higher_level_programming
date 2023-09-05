#!/usr/bin/python3
def magic_calculation(a, b, c):
    if not a < b:
        if not c > b:
            return (a * b - c)
        elif c > b:
            return (a + b)
    if a < b:
        return (c)
