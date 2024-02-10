#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """ constructor.
        attribute:
          size (int): the size of square"""
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """return the value of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value of the size.
        Attributes:
          value(int): the value of the size"""
        self.__size = value

    def area(self):
        """ function that calculate the area of the square.
        Attributes:
           no attributes.
        return:
            the area of the square."""
        area = self.__size * self.__size
        return area
