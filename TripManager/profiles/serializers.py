from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model=Profile
        fields=['id', 'user','frist_name', 'last_name','address', 'phone']
