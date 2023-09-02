from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse



class TestSetUp(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            'username': 'Prabin',
            'email': 'prabin@gmail.com',
            'password': 'hello1234567',
            'confirm_password': 'hello1234567',
        }
        return super().setUp()
    
    def tearDown(self):

        return super().tearDown()

