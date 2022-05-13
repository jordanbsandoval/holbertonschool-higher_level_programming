#!/usr/bin/python3
"""
This program will assign a random signed number to the variable number each
time it is executed.
Complete the source code in order to print the last digit of the number
stored in the variable number.
"""
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_dig = number % -10
else:
    last_dig = number % 10
print(f"Last digit of {number} is {last_dig}", end=' ')
if last_dig > 5:
    print(f"and is greater than 5")
if last_dig == 0:
    print(f"and is 0")
if last_dig < 6 and last_dig != 0:
    print(f"and is less than 6 and not 0")
