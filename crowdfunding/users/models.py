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
    ('pledges', 'Pledges'),
)


class Badge(models.Model):
    image = models.URLField()
    users = models.ManyToManyField(CustomUser, related_name="badges")
    description = models.TextField()
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES)
    badge_goal = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('badge_type', 'badge_goal'),
        )

    def __str__(self) -> str:
        return f"{self.badge_type}:{self.badge_goal}"
