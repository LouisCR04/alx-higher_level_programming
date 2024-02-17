#!/bin/bash
# Sends a JSON POST req.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
