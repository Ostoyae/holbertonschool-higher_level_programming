#!/usr/bin/python3
# script will send a request to a URL return X-Request-Id
if __name__ == "__main__":
    from sys import argv
    import requests

    if len(argv) == 2:
        res = requests.get(argv[1])
        print(res.headers['X-Request-Id'])
