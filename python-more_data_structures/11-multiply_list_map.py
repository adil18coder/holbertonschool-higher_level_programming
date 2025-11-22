#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for x in my_list:
        new_list.append(x * number)
    return new_list
