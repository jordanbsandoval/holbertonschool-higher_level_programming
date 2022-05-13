#!/usr/bin/python3
"""
Write a program that prints numbers from 0 to 99.
"""
for i in range(99):
    print("{:02}, ".format(i), end='')
print("{}".format(i+1))
