# Generated by Django 4.0.2 on 2022-04-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_rename_project_goal_project_goal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='closing_date',
            field=models.DateTimeField(null=True),
        ),
    ]
