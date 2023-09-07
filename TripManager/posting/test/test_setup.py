from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from account.models import User

class TestSetUp(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            confirm_password='testpassword'
        )
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        self.posts_url = reverse('post-list-create') 
    
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
