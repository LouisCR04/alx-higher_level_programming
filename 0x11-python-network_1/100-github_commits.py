#!/usr/bin/python3
"""Lists 10 commits (recent to oldest) from repo x by user y"""

if __name__ == "__main__":
    from sys import argv
    import requests
    req = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))
    commits = req.json()
    for com in commits[:10]:
        print(com.get('sha'), end=': ')
        print(com.get('commit').get('author').get('name'))
