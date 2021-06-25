from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from todo.models import Todo


class TodoTests(APITestCase):

    """
    Todo CRUD tests
    """

    todo_data = {'name': 'My fluendo python test.', 'completed': False}

    def setUp(self):
        self.user = User.objects.create_superuser('test_user', 'test_user@example.com', 'test_password')

        Token.objects.get_or_create(user=self.user)
        token = Token.objects.get(user__username='test_user')

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_Todo_create(self):
        url = reverse('todo-list')
        response = self.client.post(url, self.todo_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        todo = Todo.objects.get()
        self.assertEqual(todo.name, self.todo_data['name'])
        self.assertEqual(todo.user, self.user)

    def test_Todo_read(self):
        todo = Todo(**self.todo_data, user=self.user)
        todo.save()

        url = reverse('todo-detail', args=(todo.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictContainsSubset(self.todo_data, response.data)

    def test_Todo_update(self):
        todo = Todo(**self.todo_data, user=self.user)
        todo.save()

        url = reverse('todo-detail', args=(todo.id,))

        new_data = {**self.todo_data, 'completed': True}
        response = self.client.put(url, new_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.get().completed, True)

    def test_Delete_delete(self):
        todo = Todo(**self.todo_data, user=self.user)
        todo.save()

        url = reverse('todo-detail', args=(todo.id,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
