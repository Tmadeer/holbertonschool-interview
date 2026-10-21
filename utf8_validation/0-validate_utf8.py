#!/usr/bin/python3
"""Module for UTF-8 validation."""


def validUTF8(data):
    """Determine if a list of integers is a valid UTF-8 encoding.

    Args:
        data: list of integers, each representing one byte.

    Returns:
        True if data is a valid UTF-8 encoding, else False.
    """
    remaining = 0

    for num in data:
        byte = num & 255

        if remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
