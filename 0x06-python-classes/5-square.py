#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size


    @property
    def size(self):
        """print the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """prints in stdout the square with character #"""
        if self.size == 0:
            print()
        for row in range(0, self.size):
            for cal in range(0, self.size):
                print("#", end="\n" if cal == self.size -1 else "")
