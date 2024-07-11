from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name
