#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __int__(self, size=0):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
        """

        self.size = size

    @property
    def size(self):
        """Print the current size of the square.
        Returns:
            size (int)
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square.
        Args:
            value (int): new value of size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square.
        Returns:
            area
        """
        
        return self.__size ** 2
