#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {:d}".format(int(result)))
        else:
            print("Inside result: None")
    return result
