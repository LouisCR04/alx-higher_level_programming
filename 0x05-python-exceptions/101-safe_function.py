#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        div = fct(*args)
    except ZeroDivisionError as err:
        div = None
        print("Exception:", err, file=sys.stderr)
    except IndexError as er:
        div = None
        print("Exception:", er, file=sys.stderr)
    return (div)
