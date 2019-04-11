#!/bin/bash
# Bash script that takes in a URL, sends a DELETE request to the URL
curl -sfIL "$1" | grep -i Allow | awk '{$1 = ""; print $0}' | sed 's/^[ \s]//'
