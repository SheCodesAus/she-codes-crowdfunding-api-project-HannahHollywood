# Generated by Django 4.0.2 on 2022-03-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_avatar_customuser_bio_customuser_website_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='badge',
            old_name='user',
            new_name='users',
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_goal',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='badge',
            name='badge_type',
            field=models.CharField(choices=[('owner_projects', 'Project'), ('supporter_pledges', 'Pledge')], max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='badge',
            unique_together={('badge_type', 'badge_goal')},
        ),
    ]
