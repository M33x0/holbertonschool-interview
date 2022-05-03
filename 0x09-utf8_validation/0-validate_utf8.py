#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding
    Args:
        data (list): Containing dataset with multiple characters represented
            by a list of integers.
    Returns:
        boolean: True id data is valid, False otherwise
    """
    number_of_bytes = 0
    start_mask = 1 << 7
    end_mask = 1 << 6
    for number in data:
        mask = 1 << 7
        if number_of_bytes == 0:
            while mask & number:
                number_of_bytes += 1
                mask = mask >> 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (number & start_mask and not (number & end_mask)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
