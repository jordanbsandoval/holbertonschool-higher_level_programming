#!/usr/bin/python3
"""
function that finds the biggest integer of a list.
"""


def max_integer(my_list=[]):
    if my_list == None:
        return None

    num = my_list[0]
    for i in range(0, len(my_list)):
        if num < my_list[i]:
            num = my_list[i]
    return num