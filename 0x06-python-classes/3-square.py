#!/usr/bin/python3

"""Defines a square based on 2-square.py"""


class Square:
    """Instantiation witb size"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not integer:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
