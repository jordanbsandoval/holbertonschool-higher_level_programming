#!/usr/bin/python3
"""
Function that prints the last digit of a number.
"""


def print_last_digit(number):
    if number < 0:
        last_dig = number % -10
        last_dig = last_dig * -1
    else:
        last_dig = number % 10
    print(f"{last_dig}", end='')
    return (last_dig)
