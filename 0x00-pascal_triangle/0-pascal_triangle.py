#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Pascal's Triangle
    Returns a list of lists of integers representing the Pascals triangle
    Returns an empty list if n <= 0 """
    if n <= 0:
        return []
    value = [[1]]

    for i in range(n - 1):

        newRow = [0] + value[-1] + [0]

        lenrow = len(value[-1]) + 1

        valueRow = [newRow[j] + newRow[j + 1]
                    for j in range(lenrow)]

        value.append(valueRow)
    return value
