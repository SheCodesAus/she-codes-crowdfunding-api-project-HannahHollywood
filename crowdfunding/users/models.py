from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

BADGE_TYPES = (
    ('projects', 'Projects'),
    ('pledges' 'Pledges')
)

class Badge(models.Model):
    image = models.URLField()
    user = models.ManyToManyField(CustomUser, related_name="badges")
    description = models.TextField()
    badge_type = models.CharField(max_length=50, choices=BADGE_TYPES)
    badge_goal = models.PositiveIntegerField()