#!/usr/bin/python3
"""
Write a function that prints a string in uppercase followed by a new line.
"""


def uppercase(str):
    new_str = ""
    for char in str:
        if (char >= 'a') and (char <= 'z'):
            new_str = ord(char) - 32
        else:
            new_str = ord(char)
        print("{:c}".format(new_str), end='')
    print()
