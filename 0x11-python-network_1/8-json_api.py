#!/usr/bin/python3
# Post a letter to a 'http:server_ip/search_user'
if __name__ == '__main__':
    from sys import argv
    import requests

    value = {'q': '""'}
    if len(argv) == 2:
        value['q'] = argv[1]
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=value)
        if r.json():
            j = r.json()
            print('[{}] {}'.format(j['id'], j['name']))
        else:
            raise NameError
    except ValueError:
        print("Not a valid JSON")
    except NameError:
        print("No result")
