# Generated by Django 3.2.8 on 2021-11-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_alter_customeruser_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='birthday',
            field=models.DateField(verbose_name='%d/%m/%Y'),
        ),
    ]
