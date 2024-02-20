#!/usr/bin/python3
"""Sends a POST req with an email variable"""

if __name__ == "__main__":
    import requests
    from sys import argv
    values = {'email': argv[2]}
    req = requests.post(argv[1], data=values)
    print(req.text)
