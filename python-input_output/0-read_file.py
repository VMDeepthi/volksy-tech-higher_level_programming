#!/usr/bin/python3
"""Adding file"""


def read_file(filename=""):
    """files"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
