#!/usr/python3
"""
function that prints x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end="")
            count += 1
        except IndexError:
            break
    print(f"")
    return count
