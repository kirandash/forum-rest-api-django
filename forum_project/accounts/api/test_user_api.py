# reverse for generating API endpoints for test
# from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model

User = get_user_model()


class StatusTestCase(APITestCase):  # unit test
    def setUp(self):
        """Set up configuration to run before each test case"""
        # Data changes in test cases will be erased after running test
        user = User.objects.create(username='kiran',
                                   email='kiran@bgwebagency.com')
        user.set_password('django1234')
        user.save()

    # syntax: test_<somename>
    def test_creating_user(self):
        """Test if a user is created successfully using Django model"""
        qs = User.objects.filter(username='kiran')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        """Test user registration fail condition using register API"""
        url = api_reverse('api-auth:register')
        data = {
            'username': 'kiran1',
            'email': 'kiran1@bgwebagency.com',
            'password': 'django1234'
        }
        response = self.client.post(url, data, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0],
                         'This field is required.')  # check fail message

    def test_register_user_api(self):
        """Test if a user is registered successfully using register API"""
        url = api_reverse('api-auth:register')
        data = {
            'username': 'kiran1',
            'email': 'kiran1@bgwebagency.com',
            'password': 'django1234',
            'password2': 'django1234'
        }  # note this data will be erased at end of test execution
        response = self.client.post(url, data, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token_len = len(response.data.get("token", 0))  # 0 - default value
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        """Test user login fail condition using login API"""
        url = api_reverse('api-auth:login')
        data = {
            'username': 'kiran1',
            'password': 'django1234'
        }  # kiran1 does not exist
        response = self.client.post(url, data, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Invalid credentials')  # check fail message
        # check no token is returned
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_login_user_api(self):
        """Test if user is logged in successfully using login API"""
        url = api_reverse('api-auth:login')
        data = {
            'username': 'kiran',
            'password': 'django1234'
        }  # must use data from setUp. Data from other test case will be erased
        response = self.client.post(url, data, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check token is returned
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_token_login_api_fail(self):
        """Test login twice - must return forbidden"""
        url = api_reverse('api-auth:login')
        data = {
            'username': 'kiran',
            'password': 'django1234'
        }  # must use data from setUp. Data from other test case will be erased
        response = self.client.post(url, data, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check token is returned
        token = response.data.get("token", None)  # default - None
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api_fail(self):
        """Test registration after login - must return forbidden"""
        # Log In
        url = api_reverse('api-auth:login')
        data = {
            'username': 'kiran',
            'password': 'django1234'
        }  # must use data from setUp. Data from other test case will be erased
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check token is returned
        token = response.data.get("token", None)  # default - None
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # Register
        url2 = api_reverse('api-auth:register')
        data2 = {
            'username': 'kiran1',
            'email': 'kiran1@bgwebagency.com',
            'password': 'django1234',
            'password2': 'django1234'
        }  # note this data will be erased at end of test execution
        response2 = self.client.post(url2, data2, format='json')
        # print(dir(response))  # returns all props of response - debugging
        # print(response.data)
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)
