from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Menu

class APITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.staff_user = User.objects.create_user(username="staffuser", password="testpass", is_staff_member=True)
        self.menu = Menu.objects.create(name="Pizza", description="Delicious pizza", price=10.00)
        
    def test_customer_can_retrieve_menu(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('menu-detail', kwargs={'pk': self.menu.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_staff_can_create_menu(self):
        self.client.login(username="staffuser", password="testpass")
        response = self.client.post(reverse('menu-list'), {"name": "Burger", "description": "Yummy", "price": 5.00})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
