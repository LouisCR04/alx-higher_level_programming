#!/usr/bin/python3
"""Takes Github creds & uses the Github API to display ID"""

if __name__ == "__main__":
    from sys import argv
    import requests
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
