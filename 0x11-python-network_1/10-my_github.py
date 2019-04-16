#!/usr/bin/python3
# send a request to Star Wars Api
if __name__ == '__main__':
    import requests
    from sys import argv, exit

    if len(argv) < 3:
        exit()
    try:
        r = requests.get(
                'https://api.github.com/user',
                auth=(argv[1], argv[2])
                )
        r.raise_for_status()
        j = r.json()
        print(j['id'])
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.HTTPError:
        print('None')
