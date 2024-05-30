#!/usr/bin/python3
""" UTF-8 validation """


def validUTF8(data):
    """ main fuction"""
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7

        if n_bytes == 0:
            # Count number of leading 1's in the first byte
            while mask & num:
                n_bytes += 1
                mask >>= 1

            # 1 byte character
            if n_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8 encoding
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For the bytes that should follow the first byte, check for `10xxxxxx`
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
