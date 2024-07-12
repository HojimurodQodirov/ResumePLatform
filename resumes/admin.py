from django.contrib import admin
from .models import Resume, WorkPlace, News

# Register your models here.
admin.site.register([Resume, WorkPlace, News])