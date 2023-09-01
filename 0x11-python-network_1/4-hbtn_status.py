#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    text = response.text

    print(f"Body response:")
    print(f"\t- type: {type(text)}")
    print(f"\t- content: {text}")
