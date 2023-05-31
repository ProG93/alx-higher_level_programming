#!/usr/bin/python3
"""Defines a square by using a Private attribute called size"""


class Square:
    """Instantiate class with size(no type/value verification"""
    def __init__(self, size):
        self.__size = size
