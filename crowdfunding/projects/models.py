# from os import supports_bytes_environ
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# --------------------------------------
# -----------------------------------------------------------------------------------------
# --------------------------------------

# Project Creation
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    goal = models.IntegerField()
    date_created = models.DateTimeField()
    closing_date = models.DateTimeField(null=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    category = models.ForeignKey(
        'Category',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='project_id'
    )

    def save(self, **kwargs):
        super().save(**kwargs)
        # then check for badges
        self.owner.badge_check('owner_projects')

# --------------------------------------
# -----------------------------------------------------------------------------------------
# --------------------------------------

# Allow People to Pledge to Projects
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )

    def save(self, **kwargs):
        super().save(**kwargs)
        # then check for badges
        self.supporter.badge_check('supporter_pledges')

# --------------------------------------
# -----------------------------------------------------------------------------------------
# --------------------------------------

# Used to Create New Invention Categories
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

# Allow users to add Comments
class Comment(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    body = models.TextField()
    visible = models.BooleanField(default=True)