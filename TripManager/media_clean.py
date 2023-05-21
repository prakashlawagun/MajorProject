import os
from django.conf import settings
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TripManager')

# Initialize Django
django.setup()

media_root = settings.MEDIA_ROOT
media_directory = 'media'

# Get the full path of the media directory
media_directory_path = os.path.join(media_root, media_directory)

# Iterate through all files in the media directory and its subdirectories
for root, dirs, files in os.walk(media_directory_path):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.gif'):
            file_path = os.path.join(root, file)
            os.remove(file_path)
