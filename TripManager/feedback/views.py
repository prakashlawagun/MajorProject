from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from account.models import User
from .models import FeedBack
from .serializers import FeedBackSerializer

class FeedbackAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        feedbacks = FeedBack.objects.filter(user=user)
        serializer = FeedBackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        request.data['user'] = user.id
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
