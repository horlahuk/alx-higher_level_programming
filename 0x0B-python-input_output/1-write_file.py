#!/usr/bin/python3
"""Writes a string to a textfile"""


def write_file(filename="", text=""):
    """Open and write into a text file"""
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)
        return len(text)
