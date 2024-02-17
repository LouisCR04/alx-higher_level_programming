#!/bin/bash
# Sends GET req & displays body of response
curl -sX GET -H "X-School-User-Id: 98" "$1"
