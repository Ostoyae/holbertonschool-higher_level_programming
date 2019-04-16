#!/usr/bin/python3
# send a request to Star Wars Api
if __name__ == '__main__':
    import requests
    from sys import argv

    find = {'search': '', 'format': 'json'}
    if len(argv) == 2:
        find['search'] = argv[1]
    try:
        r = requests.get('https://swapi.co/api/people', params=find)
        j = r.json()
        print('Number of results: {}'.format(j['count']))
        page = j['next']
        ppl = j['results']
        while page:
            r = requests.get(page)
            page = r.json()['next']
            ppl += (r.json()['results'])
        for person in ppl:
            print("{}".format(person['name']))

    except ValueError as e:
        print(e)
        print("Not a valid JSON")
