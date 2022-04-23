from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

# Badge Type Tuple
BADGE_TYPES = (
    ('owner_projects', 'Project'),
    ('supporter_pledges', 'Pledge'),
)

# The Bades Model (two types of badges)
# 1. Projects Badges // 2. Pledge Badges
class Badge(models.Model):
    image = models.URLField()
    users = models.ManyToManyField("users.CustomUser", related_name="badges")
    description = models.TextField()
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES)
    badge_goal = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('badge_type', 'badge_goal'),
        )

    def __str__(self) -> str:
        return f"{self.badge_type}:{self.badge_goal}"

# The User Model
class CustomUser(AbstractUser):
    avatar = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username

    def badge_check(self, badge_type:str):
        """ check to see if user needs badges """
        # get the number of "badge_type" records the user has
        # e.g. badge_type = 'owner_projects
        # we will get the sum of this_user.owner_projects.count()
        # getattr is how you dynamically request an attribute from a class
        count = getattr(self, badge_type).count()
        # get a list of all the badge_ids the user already has
        existing_badge_ids = list(self.badges.filter(badge_type=badge_type).values_list('id', flat=True))
        # for each badge in the DB, check to see if the user qualifies
        for badge in Badge.objects.filter(badge_type=badge_type):
            if badge.badge_goal <= count:
                if badge.id not in existing_badge_ids:
                    self.badges.add(badge)