#!/usr/bin/python3
"""
function that returns a key with the biggest integer value.
"""


def best_score(a_dictionary):
    if a_dictionary:
        tmp = 0
        key = ""
        for k, v in a_dictionary.items():
            if v > tmp:
                tmp = v
                key = k
        return key
    else:
        return None
