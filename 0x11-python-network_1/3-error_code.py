#!/usr/bin/python3
# send a request to a url and also handle error codes
from urllib import request, error
import sys

req = request.Request(sys.argv[1])
try:
    with request.urlopen(req) as responce:
        print(responce.read().decode('utf-8'))
except error.HTTPError as e:
    print('Error code: {}'.format(e.code))
