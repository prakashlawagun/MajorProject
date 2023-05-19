from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()

