#!/usr/bin/python3
"""A square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialize a new square object
            Args:
                Size - size of the square
                x - x coordinate of the new square
                y - y coordinate of the new square
                id - id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Updates the square
            Args:
                *args(int) - new attributes value
                    - 1st argument = id attribute
                    - 2nd argument = size attribute
                    - 3rd argument = x attribute
                    - 4th argument = y attribute
                **kwargs (dict): new key/value pairs of attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of a square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }

    def __str__(self):
        """Overloading str method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
