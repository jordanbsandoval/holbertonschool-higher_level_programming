#!/usr/bin/python3
"""
function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
	if matrix:
		for ele in matrix:
			for i, num in enumerate(ele):
				print(f"{num}", end="")
				if i != 2:
					print(" ", end="")
			print()
