#!/usr/bin/python3
"""
program that prints the ASCII alphabet, in lowercase, not followed by new line
"""
for i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(i), end='')
