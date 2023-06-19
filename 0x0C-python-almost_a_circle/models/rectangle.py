#!/usr/bin/python3
from models.base import Base


"""
    class Rectangle that inherits from Base
"""


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize a new rectangle object
            Args:
                width - Rectangle width
                height - Rectangle height
                x(int) - x coordinate of rectangle
                y(int) - y coordinate of rectangle
                id(int) - id of the rectangle
            Raises:
                TypeError - if either of width, height, x or y is not int
                ValueError - if either of width or height is <= 0
                ValueError - if either of x or y is < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle instance with character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print("")

        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle

        Args:
            *args(int): new attributes values.
                - 1st argument = id attribute
                - 2nd argument = width attribute
                - 3rd argument = height attribute
                - 4th argument = x attribute
                - 5th argument = y attribute
            **kwargs (dict): represent key/value pairs of attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of a rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }

    def __str__(self):
        """Overrides the print statements"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
