#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    res = ''
    for i in str:
        res = res + chr(ord(i) - 32)
    print ('{}'.format(res))
