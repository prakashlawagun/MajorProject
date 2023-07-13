from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( 'photo', 'first_name', 'last_name', 'address', 'phone')
