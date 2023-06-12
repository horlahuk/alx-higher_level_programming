#!/usr/bin/python3
"""BaseGeometry class implementation"""


class BaseGeometry:
    """Public instance method: Area"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer
            value must be an integer
            value must be greater than 0
        """
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
