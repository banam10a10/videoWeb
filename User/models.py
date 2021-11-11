from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomerUser(AbstractUser):
    sex_choice = ((0, 'Female'), (1, 'Male'))
    avatar = models.ImageField(default='profile1.jpg', blank=True, null=True)
    birthday = models.DateField(default=date.today())
    sex = models.IntegerField(choices=sex_choice, default=1)
    address = models.CharField(default='', max_length=255)
    phone_number = models.CharField(default='', max_length=255)
