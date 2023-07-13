from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
    
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Requires user authentication

    def get(self, request, user_id):
        
        profile = get_object_or_404(Profile, user_id=user_id)
        
        # Check if the user is the owner of the profile
        if profile.user != request.user:
            return Response({'error': 'You are not the owner of this profile.'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, user_id):
        profile = get_object_or_404(Profile, user_id=user_id)
        
        # Check if the user is the owner of the profile
        if profile.user != request.user:
            return Response({'error': 'You are not the owner of this profile.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
