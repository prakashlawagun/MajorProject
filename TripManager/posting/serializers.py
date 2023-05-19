from rest_framework import serializers
from .models import Post, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['id', 'body', 'user', 'create_at']
        extra_kwargs = {'post': {'source': 'post.comment_set'}}
        

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = ['id', 'user', 'create_at']

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    

    class Meta:
        model = Post
        fields = ['id', 'user', 'body', 'photo', 'create_at', 'comments', 'likes','comment_count','like_count']
        read_only_fields = ['user', 'create_at']

    
    def get_comments(self, obj):
        comments = CommentSerializer(obj.comment_set.all(), many=True).data
        return comments
    
    def get_likes(self, obj):
        likes = LikeSerializer(obj.like_set.all(), many=True).data
        return likes
  

    
    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj).count()
