#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
    print("Inside result: {:d}".format(int(result)))
    return result
