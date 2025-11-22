#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {:d}".format(int(result)))
        except (TypeError, ValueError):
            print("Inside result: None")
    return None if result is None else result
