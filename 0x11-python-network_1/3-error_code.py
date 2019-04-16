#!/usr/bin/python3
# send a request to a url and also handle error codes
from urllib import request, error
import sys

try:
    with request.urlopen(sys.argv[1]) as responce:
        print(responce.read().decode('utf-8'))
except error.HTTPError as e:
    print('Error code: {}'.format(e.code))
