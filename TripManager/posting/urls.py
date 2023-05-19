from django.urls import path
from posting.views import PostListCreateView,PostRetrieveUpdateDeleteView,CommentCreateView,LikeCreateView,CommentDeleteView,CommentUpdateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('posts/<int:pk>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:pk>/likes/', LikeCreateView.as_view(), name='like-create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
