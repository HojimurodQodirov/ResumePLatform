from django.db import models
from django.contrib.auth.models import User
from common.models import Time


class Resume(Time):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name


class Rating(Time):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace = models.ForeignKey("WorkPlace", related_name='ratings', on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'workplace')

    def __str__(self):
        return f'{self.user.username} - {self.workplace.title}: {self.score}'


class WorkPlace(Time):
    title = models.CharField(max_length=255)
    location = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    vacation = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.title


class News(Time):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(Time):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey("Resume", related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username}: {self.comment}'