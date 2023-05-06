from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from restaurant.models import Menu
from rest_framework import status


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='user@2023')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.MenuItem1 = Menu.objects.create(title='Pizza', price=10, inventory=50)
        self.MenuItem2 = Menu.objects.create(title='Burger', price=7, inventory=30)

    def test_getall(self):
        url = reverse('MenuItem-view')
        response = self.client.get(url)
        MenuItem = MenuItem.objects.all()
        serializer = MenuSerializer(MenuItem, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assert_(response.status_code, status.HTTP_200_OK)
