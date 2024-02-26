# Generated by Django 5.0 on 2024-02-26 08:22

import core.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0003_user_comment_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=core.user.models.User.user_directory_path),
        ),
    ]
