#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked starting from the key
    contained in box 0"""
    opened = [0]
    numberOfBoxes = len(boxes)

    for box in opened:
        if box < numberOfBoxes:
            for newKey in boxes[box]:
                if newKey not in opened and 0 < newKey < numberOfBoxes:
                    opened.append(newKey)
    return True if len(opened) >= numberOfBoxes else False
