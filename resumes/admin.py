from django.contrib import admin
from .models import Resume, WorkPlace, News, Rating, Comment

# Register your models here.
admin.site.register([Resume, WorkPlace, News, Rating, Comment])