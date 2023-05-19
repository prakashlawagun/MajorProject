from django.urls import path,include
from .views import FeedbackViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'review',  FeedbackViewset)
urlpatterns = [
    path('',include(router.urls)),
]
