from django.shortcuts import render
from .models import FeedBack
from .serializers import FeedBackSerializer
from rest_framework import viewsets,permissions

# Create your views here.
class FeedbackViewset(viewsets.ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


