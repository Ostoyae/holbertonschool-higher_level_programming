#!/bin/bash
# Bash script that takes in a URL, sends a DELETE request to the URL
curl -sLf -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1" 
