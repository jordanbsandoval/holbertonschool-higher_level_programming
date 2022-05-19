#!/usr/bin/python3
"""
program that imports all functions from the file calculator_1.py
and handles basic operations
"""
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv[1:]
    operators = ['+', '-', "*", '/']
    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, b, op = argv[0], argv[2], argv[1]
    if op in operators:
        if op is operators[0]:
            print("{} {} {} = {:d}".format(a, op, b, add(int(a), int(b))))
        elif op is operators[1]:
            print("{} {} {} = {:d}".format(a, op, b, sub(int(a), int(b))))
        elif op is operators[2]:
            print("{} {} {} = {:d}".format(a, op, b, mul(int(a), int(b))))
        elif op is operators[3]:
            print("{} {} {} = {:d}".format(a, op, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
