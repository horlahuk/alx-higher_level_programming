#!/usr/bin/python3
"""open and read text files"""


def read_file(filename=""):
    """Open, read and print files"""
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
