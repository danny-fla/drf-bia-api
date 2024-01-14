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


class QuicksnapDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Quicksnap.objects.create(
            owner=adam, title='a title', content='adams content'
        )
        Quicksnap.objects.create(
            owner=brian, title='another title', content='brians content'
        )

    def test_can_retrieve_quicksnaps_using_valid_id(self):
        response = self.client.get('/quicksnap/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_quicksnaps_using_invalid_id(self):
        response = self.client.get('/quicksnap/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_quicksnaps(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/quicksnap/1/', {'title': 'a new title'})
        quicksnap = Quicksnap.objects.filter(pk=1).first()
        self.assertEqual(quicksnap.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_quicksnaps(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/quicksnap/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)