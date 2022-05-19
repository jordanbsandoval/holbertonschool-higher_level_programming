#!/usr/bin/python3
"""
Write a program that prints the number of and the list of its arguments.
"""
if __name__ == '__main__':
    import sys

    ancho = len(sys.argv[1:])
    if ancho < 1:
        print(f"{ancho} arguments.")
    elif ancho == 1:
        print(f"{ancho} argument:")
    else:
        print(f"{ancho} arguments:")

    for i in range(1, len(sys.argv[:])):
        print(f"{i}: {sys.argv[i]}")
