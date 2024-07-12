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


class WorkPlace(models.Model):
    title = models.CharField(max_length=255)
    location = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    vacation = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title