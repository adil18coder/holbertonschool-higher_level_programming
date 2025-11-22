#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    for i in my_string:
        if i=="c":
            i=" "
    my_string = "".join(my_string)
    return my_string
