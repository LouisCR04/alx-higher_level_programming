#!/bin/bash
# Displays all HTTP methods the server will accept
curl -I "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
