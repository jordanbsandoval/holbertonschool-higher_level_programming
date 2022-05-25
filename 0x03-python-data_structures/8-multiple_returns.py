#!/usr/bin/python3
"""
function that returns a tuple with the length of a string and its first charcte
"""

def multiple_returns(sentence):
    ancho = len(sentence)
    new_tuple = ()

    if ancho == 0:
        new_tuple = ancho, None
    else:
        new_tuple = ancho, sentence[0]

    return new_tuple