#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import Request, urlopen

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as response:
        content = response.read()

    print(f"Body Response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
