#!/usr/bin/python3
""" Rectangle module"""


class Rectangle:
    """ represent a rectangle"""
    def __init__(self, width=0, height=0):
        """initialization of anew instance.
        attributes:
        width(int): the width of the rectangle.
        height(int): the height of the rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ getter.return the value of the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter: set the value of the width
            Attributes:
            value(int):the value of the width"""
            if not isinstance(value, int):
                raise ValueError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ getter.return the value of the height"""
            return self.__height

        @height.setter
        def height(self, value):
            """setter:set the value of the height
            Attributes:
            value(int):the value of the height."""
            if not isinstance(value, int):
                raise ValueError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
