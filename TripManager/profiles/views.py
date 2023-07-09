from rest_framework.views import APIView
from rest_framework import permissions
from posting.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProfileListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profiles = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, user_id):
        profile = get_object_or_404(Profile, user_id=user_id, user=self.request.user)
        return profile

    def get(self, request, user_id):
        profile = self.get_object(user_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, user_id):
        profile = self.get_object(user_id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, user_id):
        profile = self.get_object(user_id)
        profile.delete()
        return Response(status=204)
