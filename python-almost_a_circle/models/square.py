#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def _init_(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""
        super()._init_(size, size, x, y, id)
