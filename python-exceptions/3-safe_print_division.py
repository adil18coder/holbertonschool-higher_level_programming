#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("Inside result: {:d}".format(int(result)))
    except ZeroDivisionError:
        print("Inside result: None")
    return result
