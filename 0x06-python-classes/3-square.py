#!/usr/bin/python3

"""Defines a square based on 2-square.py and returns the area of the square"""


class Square:
    """Instantiation witb size, raise TypeError or ValueError if size is not an int or value < 0"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
