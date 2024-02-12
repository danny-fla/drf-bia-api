from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='mike', password='pass')

    def test_can_list_recipes(self):
        mike = User.objects.get(username='mike')
        Recipe.objects.create(owner=mike, title='a title')
        response = self.client.get('/recipe/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_recipe(self):
        self.client.login(username='mike', password='pass')
        response = self.client.post('/recipe/', {'title': 'a title'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_recipe(self):
        response = self.client.post('/recipe/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Recipe.objects.create(
            owner=adam, title='a title', ingredients='adams ingredients'
        )
        Recipe.objects.create(
            owner=brian,
            title='another title',
            instructions='brians instructions'
        )

    def test_can_retrieve_recipe_using_valid_id(self):
        response = self.client.get('/recipe/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipe_using_invalid_id(self):
        response = self.client.get('/recipe/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/recipe/1/', {'title': 'a new title'})
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(recipe.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipe(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/recipe/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
