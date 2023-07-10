from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets,permissions,status
from rest_framework.response import Response


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # Include the user ID in the response data
        data = self.get_serializer(instance).data
        data['user_id'] = instance.user.id

        return Response(data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Check if the authenticated user is the owner of the profile
        if instance.user != request.user:
            return Response(
                {'error': 'You are not authorized to update this profile.'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
 