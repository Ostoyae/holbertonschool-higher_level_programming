#!/usr/bin/python3
# get me some sweet sweet tweet
if __name__ == '__main__':
    import requests
    import base64
    import sys

    c_key = bytes(sys.argv[1], 'utf-8')
    c_secret = bytes(sys.argv[2], 'utf-8')
    cat = c_key + b':' + c_secret
    mykey = base64.urlsafe_b64encode(cat)

    h = {
            'Authorization': b'Basic ' + mykey,
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8.',
            }
    grant = 'grant_type=client_credentials'
    try:
        r = requests.post(
                'https://api.twitter.com/oauth2/token',
                headers=h,
                data=grant
                )
        auth = r.json()
        post = requests.get(
                'https://api.twitter.com/1.1/search/tweets.json',
                params={
                    'q': sys.argv[3],
                    'result_type': 'recent',
                    'count': 5
                    },
                headers={'authorization': 'Bearer {}'.format(
                    auth['access_token']
                    )}
                )
        p = post.json()
        for i in p.get('statuses'):
            try:
                print('[{}] {} by {}'.format(
                    i['id'],
                    i['text'],
                    i.get('user').get('name')
                    ))
            except UnicodeEncodeError:
                print('[{}] {} by {}'.format(
                    i['id'],
                    i['text'],
                    i.get('user').get('name').encode('utf-8')
                    ))
    except ValueError as e:
        print(e)
