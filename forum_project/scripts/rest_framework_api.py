import json
import requests

ENDPOINT = "http://localhost:8000/api/status/"


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# Test: GET, DELETE, CREATE, UPDATE
do(data={'id': 7})  # data will be sent as request.body
do(method='delete', data={'id': 18})
do(method='post', data={'user': 1, "content": "some new cool content here"})
do(method='put', data={'user': 1, 'id': 7,
                       "content": "some cool content here"})
