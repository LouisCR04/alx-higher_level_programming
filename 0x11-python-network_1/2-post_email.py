#!/usr/bin/python3
"""Takes in URL & email,sends a POST req & displays body of response(utf-8)"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
