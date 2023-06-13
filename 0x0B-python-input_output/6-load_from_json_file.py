#!/usr/bin/python3
"""Object from JSON file"""
import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename) as file:
        return json.loads(file.read())
