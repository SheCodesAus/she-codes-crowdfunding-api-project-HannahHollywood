# Generated by Django 4.0.2 on 2022-03-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_user_badge_users_badge_badge_goal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='badge_type',
            field=models.CharField(choices=[('owner_projects', 'Project'), ('supporter_pledges', 'Pledge')], max_length=20),
        ),
    ]
