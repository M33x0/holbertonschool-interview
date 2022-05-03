#!/usr/bin/python3
"""UTF8 Validator"""


def validUTF8(data):
    """Checks if data is valid UTF8
    Arguments:
        data: list if integers
    Return:
        True if data is valid UTF8, False if not
    """

    # Set number of bytes to 0
    nbBytes = 0

    # masks for subsequent bytes
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Loop over each byte of the data array
    for byte in data:
        # Set mask to 10000000
        mask = 1 << 7

        # Check if current byte is a first byte
        if nbBytes == 0:
            # While the first bit is 1, shift the mask and check again,
            # incrementing the number of bytes along the way
            while byte & mask:
                nbBytes += 1
                mask = mask >> 1

            # If we're still at 0, we're on a 1 byte character, quite the loop
            if nbBytes == 0:
                continue

            # If the number of bytes is advertised as 1
            # or above 4, it's not valid utf8
            if nbBytes == 1 or nbBytes > 4:
                return False

        # If it's not a first byte and we're still here,
        # then it's a subsequent byte
        else:
            # We're on a subsequent byte that needs to start with 10.
            # If not return false
            if not (byte & mask1 and not (byte & mask2)):
                return False
        # If we get here, we're valid (up to now).
        # Decrease nbBytes and keep going
        nbBytes -= 1

    # If we end up here, we've exhausted our bytes.
    # If nbBytes is 0 the
