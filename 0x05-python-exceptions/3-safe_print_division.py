#!/usr/bin/python3
def safe_print_division(a, b):
    x = 1
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        x = 0
    finally:
        if x == 1:
            print("Inside result: {:.1f}".format(result))
            return (result)
        else:
            print("Inside result: {:s}".format("None"))
            return (None)
