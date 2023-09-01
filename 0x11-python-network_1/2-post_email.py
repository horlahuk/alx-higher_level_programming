#!/usr/bin/python3
""" Post an email to the passed url"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":

    url = argv[1]
    data = {'email': argv[2]}
    data_encoded = urlencode(data).encode('ascii')
    req = Request(url, data_encoded)

    with urlopen(req) as response:
        print(reponse.read().decode('utf-8'))
