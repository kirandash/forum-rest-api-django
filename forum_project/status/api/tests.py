# reverse for generating API endpoints for test
# from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from status.models import Status
User = get_user_model()


class StatusAPITestCase(APITestCase):  # unit test
    def setUp(self):
        """Set up configuration to run before each test case"""
        # Data changes in test cases will be erased after running test
        user = User.objects.create(username='kiran',
                                   email='kiran@bgwebagency.com')
        user.set_password('django1234')
        user.save()

        Status.objects.create(user=user, content='Test status content')

    # syntax: test_<somename>
    def test_statuses(self):
        """Test if a status is created successfully in setUp"""
        self.assertEqual(Status.objects.count(), 1)

    def status_user_token(self):
        """Helper fn to login and setup token"""
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': 'kiran',
            'password': 'django1234'
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get("token", 0)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        """Helper fn to create an item"""
        # Set token
        self.status_user_token()

        # Test status - Create
        url = api_reverse('api-status:list')
        data = {
            'content': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)
        return response.data

    def test_status_create(self):
        """Test if status create works successfully using API"""
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})

        # Testing GET method - Found
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_status_update(self):
        """Test if status update works successfully using API"""
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})
        rud_data = {
            'content': 'RUD operation data'
        }

        # Testing PUT/Update method
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        put_response_data = put_response.data
        self.assertEqual(put_response_data['content'], rud_data['content'])

    def test_status_delete(self):
        """Test if status delete works successfully using API"""
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})

        # Testing Delete method
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        """Test if status get returns 404 after delete"""
        # Testing GET method - Not Found
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token(self):
        """Test if status creation fails with no token in API"""
        # self.status_user_token()
        # Test status list
        url = api_reverse('api-status:list')
        data = {
            'content': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Status.objects.count(), 1)
