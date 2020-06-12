import os
import json
import requests

# AUTH_ENDPOINT = "http://localhost:8000/api/auth/jwt/"
AUTH_ENDPOINT = "http://localhost:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://localhost:8000/api/status/"

image_path = os.path.join(os.getcwd(), "testimage.png")

data = {
    'username': 'kiran',
    'password': 'django1234'
}

r = requests.post(AUTH_ENDPOINT, data=data)

# alternate way to post with with headers
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)

print(r.json())  # should print response with token in console

token = r.json()  # ['token']

print(token)  # print token in console

# Store the token in cookie and set expiration date (Frontend)

# Test request for REFRESH ENDPOINT
# headers = {
#     "Content-Type": "application/json"
# }
#
# refresh_data = {
#     'token': token
# }
#
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data),
#                              headers=headers)
# new_token = new_response.json()['token']
#
# print(new_token)  # should print refreshed/renewed token in console
#
# get_endpoint = ENDPOINT + str(12)
# post_data = json.dumps({"content": "Some random content posted with jwt"})
#
# # GET calls should run fine without auth
# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# # POST Calls will ask for auth
# post_headers = {
#     'content-type': 'application/json',
#     "Authorization": "JWT " + token,
# }
# # post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
#
# print(post_response.text)
#
#
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {
#         'Authorization': "JWT " + token
#     }
#     if is_json:
#         # JWT from DRF auto adds content type as json. No need to force
#         # headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             if method == 'put':
#                 r = requests.request(method, ENDPOINT + str(data['id']) + '/',
#                                      data=data,
#                                      headers=headers, files=file_data)
#             else:
#                 r = requests.request(method, ENDPOINT, data=data,
#                                      headers=headers, files=file_data)
#     else:
#         if method == 'put':
#             r = requests.request(method, ENDPOINT + str(data['id']) + '/',
#                                  data=data,
#                                  headers=headers)
#         else:
#             r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
#
# # do_img(method='post', data={'user': 1, 'content': ''},
# #        is_json=False, img_path=image_path)
# # do_img(method='put', data={'user': 1, 'id': 21,
# #        'content': 'new content here'},
# #        is_json=False, img_path=image_path)
# do_img(method='post', data={'content': ''}, is_json=False, img_path=image_path)
# do_img(method='put', data={'id': 39, 'content': 'putting 39 content here'},
#        is_json=False, img_path=image_path)
#
#
# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# Test: GET, DELETE, CREATE, UPDATE
# do(data={'id': 7})  # data will be sent as request.body
# do(method='delete', data={'id': 18})
# do(method='post', data={'user': 1, "content": "some new cool content here"})
# do(method='put', data={'user': 1, 'id': 7,
#                        "content": "some cool content here"})
