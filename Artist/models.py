from datetime import date, datetime

from django.db import models

# Create your models here.
class Artist(models.Model):
    sex_choice = ((0, 'Female'), (1, 'Male'))
    Name = models.CharField(default="", max_length=255)
    RealName = models.CharField(default="", max_length=255)
    birthday = models.DateField(default= f"{date.today()}")
    image = models.ImageField(upload_to='images')
    sex = models.IntegerField(choices=sex_choice, default=1)
    homeland = models.CharField(default='',max_length=255)
    description = models.TextField(default='')
    def __str__(self):
        return self.Name