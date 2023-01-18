#!/usr/bin/python3
"""load json file"""


import json


def load_from_json_file(filename):
    """files"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
