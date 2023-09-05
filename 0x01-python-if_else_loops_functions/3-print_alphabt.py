#!/usr/bin/python3
for w in range(ord('a'), ord('z') + 1):
    if w is ord('q') or w is ord('e'):
        continue;
    print('{}'.format(chr(w)), end="")
