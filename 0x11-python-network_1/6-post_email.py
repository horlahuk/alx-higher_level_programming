#!/usr/bin/python3
"""post an email"""
from sys import argv
from requests import post

if __name__ == "__main__":
    req = post(argv[1], {'email': argv[2]})
    print(req.text)
