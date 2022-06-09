#!/usr/bin/python3
"""
function that divides 2 integers and prints the result.
"""


def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print(f"Inside result: {res}")
        return res
