from django.db import models

# Create your models here.
class Time(models.Model):
    created_time = models.DateTimeField(auto_created=True)
    updated_time = models.DateTimeField(auto_now=True)