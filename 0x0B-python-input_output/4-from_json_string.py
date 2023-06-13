#!/usr/bin/python3
"""Object represented by a JSON string"""
import json


def from_json_string(my_obj):
    """returns object represented by JSON string"""
    return json.loads(my_obj)
