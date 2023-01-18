#!/usr/bin/python3
"""save"""


import json


def save_to_json_file(my_obj, filename):
    """files"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
