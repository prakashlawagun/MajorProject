from django.shortcuts import render
from .models import Profile
from.serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from posting.permissions import IsOwnerOrReadOnly

# Create your views here.
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

