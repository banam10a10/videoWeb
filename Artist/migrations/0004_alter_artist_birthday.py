# Generated by Django 3.2.8 on 2021-11-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artist', '0003_auto_20211028_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birthday',
            field=models.DateField(default='2021-11-07'),
        ),
    ]
