#!/usr/bin/python3
"""append"""


def append_write(filename="", text=""):
    """files"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
