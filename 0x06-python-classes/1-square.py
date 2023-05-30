#!/usr/bin/python3

"""Defines a class Square with a private instance attribute: size"""


class Square:
    """Instantiate size with no type/value verification"""
    def __init__(self, size):
        self.__size = size
