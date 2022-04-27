#!/usr/bin/python3
"""
This method that calculates the fewest number of
operations needed to result
in exactly n H characters in the file
"""


def minOperations(n):
    """
    Method that calculates the fewest number of operations
    n H charcacters in the file.
    """

    count = 1
    numValue = 0
    buffer = 0

    if n < 2:
        return 0

    while count < n:
        rest = n - count

        if rest % count == 0:
            buffer = count
            count += buffer
            numValue += 2

        else:
            count += buffer
            numValue += 1

    return numValue
