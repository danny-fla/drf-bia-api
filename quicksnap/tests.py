from django.contrib.auth.models import User
from .models import Quicksnap
from rest_framework import status
from rest_framework.test import APITestCase


class QuicksnapListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='mike', password='pass')

    def test_can_list_quicksnaps(self):
        mike = User.objects.get(username='mike')
        Quicksnap.objects.create(owner=mike, title='a title')
        response = self.client.get('/quicksnap/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_quicksnaps(self):
        self.client.login(username='mike', password='pass')
        response = self.client.post('/quicksnap/', {'title': 'a title'})
        count = Quicksnap.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_quicksnaps(self):
        response = self.client.post('/quicksnap/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)