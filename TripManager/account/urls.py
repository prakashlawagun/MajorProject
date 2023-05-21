from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView,UserDeleteView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('change-password/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]
