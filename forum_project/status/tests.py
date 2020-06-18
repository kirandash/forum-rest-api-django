from django.test import TestCase


from django.contrib.auth import get_user_model
from .models import Status
User = get_user_model()


class StatusTestCase(TestCase):  # unit test
    def setUp(self):
        # Data changes in test cases will be erased after running test
        user = User.objects.create(username='kiran',
                                   email='kiran@bgwebagency.com')
        user.set_password('django1234')
        user.save()

    # syntax: test_<somename>
    def test_creating_status(self):
        user = User.objects.get(username='kiran')  # since only 1 user
        obj = Status.objects.create(user=user, content='Test cool contente')

        self.assertEqual(obj.id, 1)
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)
