from django.urls import path
from .views import FeedbackAPIView

urlpatterns = [
    path('review/<int:user_id>/', FeedbackAPIView.as_view(), name='feedback-api'),
]
