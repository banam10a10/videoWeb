# Generated by Django 3.2.8 on 2021-10-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0002_alter_artist_birthday'),
        ('Video', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auhtor',
            new_name='Author',
        ),
    ]