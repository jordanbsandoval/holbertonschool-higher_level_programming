#!/usr/bin/python3
"""
function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print(f"wrong type")
            result = 0
        except ZeroDivisionError:
            print(f"division by 0")
            result = 0 
        except IndexError:
            print(f"out of range")
            result = 0 
        finally:
            new_list.append(result)
    return new_list