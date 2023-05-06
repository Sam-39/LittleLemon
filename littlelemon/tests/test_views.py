from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        self.pizza = Menu.objects.create(title='Pizza', price=10, inventory=50)
        self.burger = Menu.objects.create(title='Burger', price=7, inventory=20)
    