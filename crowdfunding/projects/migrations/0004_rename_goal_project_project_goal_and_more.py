# Generated by Django 4.0.2 on 2022-03-25 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_pledge_supporter_alter_project_goal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='goal',
            new_name='project_goal',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='project_image',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='project_title',
        ),
    ]