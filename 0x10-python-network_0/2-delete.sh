#!/bin/bash
# Bash script that takes in a URL, sends a DELETE request to the URL
curl -sfL -X DELETE "$1"
