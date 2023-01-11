#!/usr/bin/python3
"""string size"""


class Square:
    '''size'''
    def __init__(square, size=0):

        if type(size) != int:
            raise typeerror("value is not integer")
        if size < 0:
            raise valueerror("value is less than 0")

        square.__size = size

    def area(square):
        return square.__size*square.__size
