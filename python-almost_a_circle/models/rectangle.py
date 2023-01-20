#!/usr/bin/python3
"""This module provides a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute number_of_instances that keeps track of # of instances,
    and class attribute print_symbol which is used as symbol for printing.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
   @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x"""
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """y"""
        self.__y = value
