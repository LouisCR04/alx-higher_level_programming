#!/usr/bin/python3
"""Taskes in a URL, sends req & displays value of X-Request-Id"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
