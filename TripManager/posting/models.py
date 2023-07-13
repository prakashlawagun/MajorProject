from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(upload_to='media',blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    body = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username




