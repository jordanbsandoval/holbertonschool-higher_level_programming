#!/usr/bin/python3
"""
function that replaces an element in a list at a specific
position without modifying the original list
"""


def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        new_list.append(i)
    new_list[idx] = element
    return new_list
