#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""

    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line,
        and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module

"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
