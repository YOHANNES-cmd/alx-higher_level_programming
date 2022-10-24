#!/usr/bin/python3
"""
This is module 7-base_geometry

This module contains:
-one class
-two functions

Access test for this class in /tests subfolder - to run:
`python3 -m doctest ./tests/7-base_geometry.txt`
"""


class BaseGeometry:
    """
    base geometry class

    Public instance method:
    `def area(self)`
    `def integer_validator(self, name, value)`

    Args:
    name
    value
    Returns:
    area of shape
    """

    def area(self):
        """
        public method to determine area
        Raises:
        Exception with the message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value from int type
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
