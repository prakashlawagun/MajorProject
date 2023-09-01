from django.db import models
from account.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.user.username
