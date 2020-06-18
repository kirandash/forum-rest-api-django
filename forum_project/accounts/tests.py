from django.test import TestCase


from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):  # unit test
    def setUp(self):
        # Data changes in test cases will be erased after running test
        user = User.objects.create(username='kiran',
                                   email='kiran@bgwebagency.com')
        user.set_password('django1234')
        user.save()

    # syntax: test_<somename>
    def test_created_user(self):
        qs = User.objects.filter(username='kiran')
        self.assertEqual(qs.count(), 1)
