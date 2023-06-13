#!/usr/bin/python3
"""Add arguments to a list and save to a file"""
import sys
import json


save_to_json = __import__('5-save_to_json_file')
load_from_json = __import__('6-load_from_json_file')


def add_items():
    """adds all arguments to a list"""
    filename = "add_item.json"
    try:
        my_list = load_from_json(filename)
    except FileNotFoundError:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json(my_list, filename)
