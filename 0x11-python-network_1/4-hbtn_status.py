#!/usr/bin/python3
"""Fetches from URL X using requests package"""

if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    html = req.text

    print("Body response:\n\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
