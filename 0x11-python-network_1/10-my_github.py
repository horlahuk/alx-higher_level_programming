#!/usr/bin/python3
"""Github API"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=authentication)

    print(r.json().get("id"))
