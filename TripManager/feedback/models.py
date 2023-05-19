from django.db import models
from account.models import User

# Create your models here.
class FeedBack(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    emoji = models.CharField(max_length=10)
    body = models.TextField()
    ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

