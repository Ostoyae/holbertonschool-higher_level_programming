#!/usr/bin/python3
# send a request to a url and also handle error codes
import urllib
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as responce:
        print(responce.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error code: {}'.format(e.code))
