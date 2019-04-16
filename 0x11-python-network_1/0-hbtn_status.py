#!/usr/bin/python3
# This script fetches the body from https://intranet.hbtn.io/status
from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as responce:
    print('Body response:')
    html = responce.read()
    cont = html.decode('utf-8')
    print("    - type: {}".format(type(responce.read())))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(cont))
