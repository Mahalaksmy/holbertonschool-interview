#!/usr/bin/python3
"""This is  a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""

    value = [0]

    if len(boxes) == 0:
        return True

    for i in value:
        for x in boxes[i]:
            if x not in value and x < len(boxes):
                value.append(x)

    return len(value) == len(boxes)

