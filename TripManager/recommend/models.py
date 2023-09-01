from django.db import models
from account.models import User


class Recommendation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    response = models.JSONField(null=True)  # Store the response as JSON data

    def __str__(self):
        return self.query
