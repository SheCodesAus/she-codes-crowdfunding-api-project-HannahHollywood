# from os import supports_bytes_environ
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    description = models.TextField()
    project_image = models.URLField()
    is_open = models.BooleanField()
    project_goal = models.IntegerField()
    date_created = models.DateTimeField()
    # owner = models.CharField(max_length=200)
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
    # categories = models.ManyToManyField(Category, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
