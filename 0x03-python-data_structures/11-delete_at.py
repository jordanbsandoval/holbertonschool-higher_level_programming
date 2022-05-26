#!/usr/bin/python3
"""
function that deletes the item at a specific position in a list.
"""


def delete_at(my_list=[], idx=0):
    len_lista = len(my_list)
    new_list = []

    if idx > len_lista:
        return my_list

    for i in range(len_lista):
        if i == idx:
            del my_list[i]
    return my_list
