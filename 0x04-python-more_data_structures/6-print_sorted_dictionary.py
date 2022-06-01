#!/usr/bin/python3
"""
function that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for keys, valor in sorted(a_dictionary.items()):
            print(f"{keys} : {valor}")
        