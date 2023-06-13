#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """a new class, Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle class
        Args:
            width(int): rectangle width
            height(int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle with #"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for h in range(self.__height):
            for w in range(self.__width):
                rect = rect + '#'
            if h != self.__height - 1:
                rect = rect + '\n'
        return rect

    def __repr__(self):
        """print string representation of rectangle"""
        x = "Rectangle(" + str(self.__width) + ', ' + str(self.__height) + ')'
        return x