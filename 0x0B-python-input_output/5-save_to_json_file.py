#!/usr/bin/python3
"""Object to a text file, using JSON representation"""
import json


def save_to_json_file(my_obj, filename=""):
    """writes an object to a text file, using JSON"""
    with open(filename, "w", encoding="utf8") as file:
        json.dump(my_obj, file)
