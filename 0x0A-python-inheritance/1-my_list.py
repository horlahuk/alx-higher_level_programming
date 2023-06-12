#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """prints a sorted list of list"""
        sorted_list = self[:]
        sorted_list = sorted(sorted_list)
        print(sorted_list)
        return sorted_list
