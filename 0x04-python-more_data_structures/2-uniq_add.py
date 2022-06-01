#!/usr/bin/python3
"""
function that adds all unique integers in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    if my_list:
        setty = set(my_list)
        n = 0
        for item in setty:
            n += item
        return n
    else:
        return 0
