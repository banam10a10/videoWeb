# Generated by Django 3.2.8 on 2021-11-07 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0006_auto_20211107_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='User',
        ),
    ]
