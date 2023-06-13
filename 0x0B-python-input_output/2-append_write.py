#!/usr/bin/python3
"""Append text to a file"""


def append_write(filename="", text=""):
    """append text in to filename"""
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
        return len(text)
