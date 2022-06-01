#!/usr/bin/python3
"""
 function that replaces all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    if my_list and search and replace:
        new_list = [item if item != search else replace for item in my_list]
        return new_list
    else:
        return my_list
