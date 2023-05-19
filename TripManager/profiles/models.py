from django.db import models
from account.models import User
from django.core.validators import RegexValidator

# Create your models here.
# phone_regex = RegexValidator(
#     regex=r'^\+?977?d{10}',
#     message="Phone number must be entered in the format: '+977999999999."
# )

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username