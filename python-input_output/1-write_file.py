#!/usr/bin/python3
"""write files"""


def write_file(filename="", text=""):
    """files"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
