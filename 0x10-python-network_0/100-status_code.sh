#!/bin/bash
# Sends a req & returns status code
curl -so /dev/null --write-out "%{http_code}" "$1"
