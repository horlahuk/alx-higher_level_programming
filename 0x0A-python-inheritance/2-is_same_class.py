#!/usr/bin/python3
"""checks if obj is an instance of a_class"""


def is_same_class(obj, a_class):
    """uses type to check for instance"""
    if type(obj) is a_class:
        return True
    else:
        return False
