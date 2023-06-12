#!/usr/bin/python3
"""checks if object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """use isinstance to check for instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
