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
