import os
import shutil  # shell utility module
import tempfile
from PIL import Image  # pip install pillow

# reverse for generating API endpoints for test
# from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.settings import api_settings

from status.models import Status

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

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

    def test_create_empty_item(self):
        """Test creating a status item with no content and image"""
        # Set token
        self.status_user_token()

        # Test status - Create
        url = api_reverse('api-status:list')
        data = {
            'content': '',
            'image': ''
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
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

    def test_status_create_with_image(self):
        """Test if status create with img works successfully using API"""
        self.status_user_token()
        url = api_reverse('api-status:list')
        # (w, h) = (800, 1280)
        # (R, G, B) = (255, 255, 255)
        # create a dummy image item - will be created in media-root
        image_item = Image.new('RGB', (800, 1280), (255, 255, 255))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        # rb: read bytes - open image file data
        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'content': 'Some fun content',
                'image': file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.count(), 2)
            # print(response.data)
            # check if image url is returned in response after upload
            img_data = response.data.get('image')
            self.assertNotEqual(img_data, None)

        # After testing, image is removed from db but still stays in media-root
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'kiran')

        if os.path.exists(temp_img_dir):
            # removes the entire directory. check later to remove only file
            shutil.rmtree(temp_img_dir)

    def test_status_create_with_image_no_content(self):
        """Test if status create with img and no content works"""
        self.status_user_token()
        url = api_reverse('api-status:list')
        # (w, h) = (800, 1280)
        # (R, G, B) = (255, 255, 255)
        # create a dummy image item - will be created in media-root
        image_item = Image.new('RGB', (800, 1280), (255, 255, 255))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        # rb: read bytes - open image file data
        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'content': '',
                'image': file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Status.objects.count(), 2)
        # After testing, image is removed from db but still stays in media-root
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'status', 'kiran')

        if os.path.exists(temp_img_dir):
            # removes the entire directory. check later to remove only file
            shutil.rmtree(temp_img_dir)

    def test_other_user_permissions_api(self):
        """Test accessing Status of other user"""
        data = self.create_item()
        data_id = data.get("id")
        user = User.objects.create(username='kirandash')
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        rud_url = api_reverse('api-status:detail', kwargs={"id": data_id})
        rud_data = {
            'content': 'smashing'
        }
        get_ = self.client.get(rud_url, format='json')
        put_ = self.client.put(rud_url, rud_data, format='json')
        delete_ = self.client.delete(rud_url, format='json')

        self.assertEqual(get_.status_code, status.HTTP_200_OK)
        self.assertEqual(put_.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete_.status_code, status.HTTP_403_FORBIDDEN)
