#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Initiate object size"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): the size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Return the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the current size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2
