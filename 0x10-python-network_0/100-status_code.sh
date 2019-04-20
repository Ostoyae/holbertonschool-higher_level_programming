#!/bin/bash
# get status code
curl -so /dev/null -I -w "%{http_code}" "$1"
