import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TripManager.settings')
django.setup()

from account.models import User
User.objects.create_superuser(username='admin', email='admin@example.com', password='password')

