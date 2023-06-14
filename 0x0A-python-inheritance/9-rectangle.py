#!/usr/bin/python3
"""Rectangle class implementation"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry class"""
    def __init__(self, width, height):
        """Instantiatiom with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
