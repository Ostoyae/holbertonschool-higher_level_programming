#!/usr/bin/python3
# script will send a request to a URL return X-Request-Id
from urllib import request
from sys import argv

if len(argv) == 2:
    with request.urlopen(argv[1]) as responce:
        header = responce.info()
        print(header['X-Request-Id'])
