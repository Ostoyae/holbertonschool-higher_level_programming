#!/usr/bin/python3
# This script fetches the body from https://intranet.hbtn.io/status
import requests

response = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
