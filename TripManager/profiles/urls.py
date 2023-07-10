from django.urls import include, path
from rest_framework import routers
from profiles.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
