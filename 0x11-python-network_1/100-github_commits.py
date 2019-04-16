#!/usr/bin/python3
# return the last 10 commits for a specific repo
if __name__ == '__main__':
    import requests
    import sys
    if len(sys.argv) != 3:
        sys.exit()
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{o}/{r}/commits'.format(
        r=repo, o=owner)
    try:
        r = requests.get(url)
        commits = r.json()
        for i in range(10):
            try:
                c = commits[i]
                sha = c.get('sha')
                author = c.get('commit').get('author').get('name')
                print('{}: {}'.format(sha, author))
            except IndexError:
                break
            except UnicodeEncodeError:
                print('{}: {}'.format(sha, author.encode('latin1')))
    except ValueError as e:
        print(e)
