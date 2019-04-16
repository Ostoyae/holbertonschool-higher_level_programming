#!/usr/bin/python3
# script will send a post to a URL
if __name__ == "__main__":
    from sys import argv
    import requests

    try:
        res = requests.post(argv[1], data={'email': argv[2]})
        print(res.text)
    except Exception:
        pass
