from rest_framework import serializers
from .models import FeedBack

class FeedBackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = FeedBack
        fields = ['id','user','emoji','body','ratings','created_at']
        
   