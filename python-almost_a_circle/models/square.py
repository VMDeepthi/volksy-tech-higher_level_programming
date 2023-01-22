#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""

        super().__init__(size, size, x, y, id)

def _str_(self):
    """return string representation of Rectangle"""
    return '[' + type(self)._name_ + '] (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - ' \
            + str(self.size)        
