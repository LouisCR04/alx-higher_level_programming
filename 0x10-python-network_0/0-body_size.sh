#!/bin/bash
# Takes in url, sends req to it, displays size of its body
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
