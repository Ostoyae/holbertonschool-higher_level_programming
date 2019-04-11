#!/bin/bash
# used curl to get the byte size of the content.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
