from django.urls import path
from profiles.views import ProfileListCreateAPIView, ProfileDetailAPIView

urlpatterns = [
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:user_id>/', ProfileDetailAPIView.as_view(), name='profile-detail'),
]
