#!/usr/bin/python3
"""
Determines if a given data set represents 
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing the bytes of the data set
    :return: True if the data is valid UTF-8 encoding, else False
    """
    bytes_to_check = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if bytes_to_check == 0:
            if (byte >> 5) == 0b110:
                bytes_to_check = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_check = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_check = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0
