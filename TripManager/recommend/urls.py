from django.urls import path
from .views import RecommendationAPIView

urlpatterns = [
    path('recommendations/', RecommendationAPIView.as_view(), name='recommendations'),
    path('history/<int:user_id>/', RecommendationAPIView.as_view(), name='history'),
    
]
