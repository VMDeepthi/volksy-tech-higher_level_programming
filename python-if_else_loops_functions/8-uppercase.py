#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    res = ''
    for i in str:
        if ord(i) > 96:
            res = res + chr(ord(i) - 32)
        else:
            res = res + i
    print('{}'.format(res)i)
