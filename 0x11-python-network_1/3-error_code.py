#!/usr/bin/python3
# send a request to a url and also handle error codes
from urllib import request
from urllib.error import HTTPError
from sys import argv, exit

if len(argv) == 1:
    exit()

try:
    with request.urlopen(argv[1]) as responce:
        print(responce.read().decode('utf-8'))
except HTTPError as e:
    print('Error code: {}'.format(e.code))
