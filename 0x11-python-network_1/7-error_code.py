#!/usr/bin/python3
# script will send a GET to a URL and return body if status 200 else print 
# the status code 
if __name__ == "__main__":
    from sys import argv
    import requests

    try:
        res = requests.get(argv[1])
        res.raise_for_status()
        print(res.text)
    except Exception as e:
        print("Error code: {}".format(res.status_code))
