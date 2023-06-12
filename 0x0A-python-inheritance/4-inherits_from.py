#!/usr/bin/python3
"""checks for instance of a class that inherited from another class"""


def inherits_from(obj, a_class):
    """use issubclass to check for inheritance"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
