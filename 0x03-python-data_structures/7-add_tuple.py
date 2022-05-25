#!/usr/bin/python3
"""
function that adds 2 tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    new_list = [0, 0]
    for i in range(len(tuple_b)):
        new_list[i] = tuple_b[i]

    for i in range(len(tuple_a)):
        new_list[i] += tuple_a[i]
    return (tuple(new_list))
