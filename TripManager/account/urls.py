from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView,UserDeleteView,PasswordResetSuccessView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('change-password/<int:user_id>/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<str:uid>/<str:token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('password-reset-success/', PasswordResetSuccessView.as_view(), name='password-reset-success'),

]
