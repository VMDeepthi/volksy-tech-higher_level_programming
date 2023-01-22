#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""

        super().__init__(size, size, x, y, id)        
