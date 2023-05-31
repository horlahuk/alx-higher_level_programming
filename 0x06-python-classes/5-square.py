#!/usr/bin/python3

"""Define a class"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): the size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Return the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the curreng size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of the current square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with #"""
        if self.size == 0:
            print()
        for row in range(0, self.size):
            for col in range(0, self.size):
                print("#", end="\n" if col == self.size - 1 else "")
