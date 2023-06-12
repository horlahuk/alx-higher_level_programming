#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints a sorted list of list"""
        print(sorted(self))
