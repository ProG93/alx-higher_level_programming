#!/usr/bin/python3
"""Add two integers"""


def add_integer(a, b=98):
    """Function that adds two integers.
    Args:
        a(int or float): first integer.
        b(int or float): second integer. equals to 98.
    Return:
        int: the sum of the two integers.
    """
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    return int (a) + int (b)
