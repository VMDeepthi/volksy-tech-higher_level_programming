#!/usr/bin/python3
"""write file"""


def number__of__lines(filename=""):
    """files"""
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
