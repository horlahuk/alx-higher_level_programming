#!/usr/bin/python3
"""Error code #1"""
from sys import argv
from requests import post

if __name__ == "__main__":
    req = post(argv[1], {'email': argv[2]})
    print(req.text)
