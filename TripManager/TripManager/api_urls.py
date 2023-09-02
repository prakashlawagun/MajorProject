from django.urls import path, include
urlpatterns = [
    path('user/', include('account.urls')),
    path('post/', include('posting.urls')),
    path('profile/', include('profiles.urls')),
    path('feedback/', include('feedback.urls')),
    path('notification/', include('email_notification.urls')),
    path('recommendation/', include('recommend.urls')),
    
]