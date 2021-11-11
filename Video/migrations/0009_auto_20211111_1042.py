# Generated by Django 3.2.8 on 2021-11-11 03:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Video', '0008_video_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='Dislike',
        ),
        migrations.AddField(
            model_name='video',
            name='Dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislike_Video', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='video',
            name='Likes',
        ),
        migrations.AddField(
            model_name='video',
            name='Likes',
            field=models.ManyToManyField(blank=True, related_name='like_Video', to=settings.AUTH_USER_MODEL),
        ),
    ]
