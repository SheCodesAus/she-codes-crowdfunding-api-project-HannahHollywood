from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Profile(models.Model):
    username = models.CharField(max_length=200)
    full_name = models.CharField(max_length=600)
    avatar = models.URLField()
    bio = models.CharField(max_length=600)
    website = models.URLField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile'
    )

class Badge(models.Model):
    image = models.URLField()
    user = models.ManyToManyField(CustomUser, related_name="badges")
    description = models.TextField()
    badge_type = models.CharField(max_length=50)