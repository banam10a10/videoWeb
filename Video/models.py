from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.http import request

from Artist.models import Artist
from User.models import CustomerUser


class Category(models.Model):
    Name = models.CharField(default='',max_length=255)
    descrition = models.TextField()
    def __str__(self):
        return self.Name

class Video(models.Model):
    Title = models.CharField(default='',max_length=255)
    Thumbnail = models.ImageField(upload_to='images',default='profile1.jpg',blank=True,null=True)
    Location = models.FileField(upload_to='Videos_Upload')
    Description = models.TextField(default='')
    Category = models.ForeignKey(Category, on_delete= models.CASCADE)
    User = models.ForeignKey(CustomerUser, on_delete= models.DO_NOTHING)
    view = models.IntegerField(default=0)
    Likes = models.ManyToManyField(CustomerUser,blank=True,related_name='like_Video')
    Dislikes = models.ManyToManyField(CustomerUser,blank=True,related_name='dislike_Video')

    def __str__(self):
        return self.Title

    def total_like(self):
        return self.Likes.count()

    def total_dislike(self):
        return self.Dislikes.count()

class Author(models.Model):
    VideoId = models.ForeignKey(Video, on_delete= models.CASCADE)
    ArtistId = models.ForeignKey(Artist, on_delete= models.CASCADE)



