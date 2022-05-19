#!/usr/bin/python3
"""
Write a program that prints the result of the addition of all arguments
"""

if __name__ == '__main__':
    import sys
    result = 0
    for i in sys.argv[1:]:
        result += int(i)
    print(f"{result}")

