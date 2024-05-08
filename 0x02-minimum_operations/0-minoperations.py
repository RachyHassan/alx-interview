#!/usr/bin/python3
"""
A function that calculated the least number of operations
"""


def minOperations(n):
    """
    minOperation: a function to calculate least number of operations
    """
    if n <= 1:  # no operation is needed for one number
        return 0
    div = 2  # Breaking down the numbers
    no_of_operations = 0

    while n > 1:  # e.g 2
        if n % div == 0:  # 2 % 2 = 0
            n = n / div  # 2 = 2/2 = 1

            no_of_operations = no_of_operations + div  # 0 + 2 = 2

        else:
            div += 1
    return no_of_operations
