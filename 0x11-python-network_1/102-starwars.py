#!/usr/bin/python3
# send a request to Star Wars Api
import requests

def get_film_title(film={}, key=""):
    if key in film:
        return film[key]
    else:
        try:
            r = requests.get(key, params={'format': 'json'})
            title = r.json()['title']
            film.update({key: title})
            return title
        except ValueError:
            print("whoops")
        
    
if __name__ == '__main__':
    import requests
    from sys import argv

    movies = dict()
    errors = 0
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
            try:
                print("{}".format(person['name']))

                for film in person['films']:
                    print('\t{}'.format(get_film_title(movies, film)))
            except ValueError:
                errors += 1
    except ValueError as e:
        print(e)
        print("Not a valid JSON")

    if errors:
        print("{} happen due to ascii encoding issues".format(errors))
