import os
import json
import requests

ENDPOINT = "http://localhost:8000/api/status/"

image_path = os.path.join(os.getcwd(), "testimage.png")


def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data,
                                 headers=headers, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


do_img(method='post', data={'user': 1, 'content': ''},
       is_json=False, img_path=image_path)
do_img(method='put', data={'user': 1, 'id': 21, 'content': 'new content here'},
       is_json=False, img_path=image_path)


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
# do(data={'id': 7})  # data will be sent as request.body
# do(method='delete', data={'id': 18})
# do(method='post', data={'user': 1, "content": "some new cool content here"})
# do(method='put', data={'user': 1, 'id': 7,
#                        "content": "some cool content here"})