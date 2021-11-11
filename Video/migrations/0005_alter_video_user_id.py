# Generated by Django 3.2.8 on 2021-11-07 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Video', '0004_video_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
