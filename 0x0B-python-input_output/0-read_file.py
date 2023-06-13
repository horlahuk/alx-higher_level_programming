#!/usr/bin/python3

def read_file(filename=""):
    """Open and read files"""
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            print(line, end="")
