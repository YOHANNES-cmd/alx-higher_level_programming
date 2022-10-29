#!/usr/bin/python3
"""The Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """The Recatangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        "Initialize an object"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints a drawing of rectangle with "#" symbol"""
        print("\n" * self.__y + "\n".join((" " * self.__x + "#" * self.__width)
                                          for x in range(self.__height)))

    def __str__(self):
        """Representation of rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates attributes of a rectangle object"""
        attributes = ["id", "width", "height", "x", "y"]
        for atrr, arg in zip(attributes, args):
            setattr(self, atrr, arg)
        for atrr, arg in kwargs.items():
            setattr(self, atrr, arg)

    def to_dictionary(self):
        """return dictionnary of rectangle attributes"""
        atrributes = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in atrributes}
