from rest_framework import serializers
from .models import FeedBack

class FeedBackSerializer(serializers.ModelSerializer):
 

    class Meta:
        model = FeedBack
        fields = ['id','user','emoji','body','ratings','created_at']
        
   