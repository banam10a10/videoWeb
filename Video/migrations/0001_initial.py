# Generated by Django 3.2.8 on 2021-10-28 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=255)),
                ('descrition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=255)),
                ('Thumbnail', models.ImageField(blank=True, default='profile1.jpg', null=True, upload_to='images')),
                ('Location', models.FileField(upload_to='Videos_Upload')),
                ('Description', models.TextField(default='')),
                ('Likes', models.IntegerField(default=0)),
                ('Dislike', models.IntegerField(default=0)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Video.category')),
            ],
        ),
        migrations.CreateModel(
            name='Auhtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArtistId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Artist.artist')),
                ('VideoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Video.video')),
            ],
        ),
    ]
