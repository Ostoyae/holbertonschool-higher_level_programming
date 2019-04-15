#!/usr/bin/python3
# send a email
from urllib import parse, request
from sys import argv

if len(argv) == 3:
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as responce:
        print(responce.read().decode('utf-8'))
