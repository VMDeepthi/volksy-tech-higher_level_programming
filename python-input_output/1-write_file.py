#!/usr/bin/python3
"""write file"""


def number_of_lines(filename=""):
    """file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
