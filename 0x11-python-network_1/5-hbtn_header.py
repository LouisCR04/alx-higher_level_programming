#!/usr/bin/python3
"""Displays value in var X-Request-Id in header"""

if __name__ == "__main__":
    import requests
    from sys import argv
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
