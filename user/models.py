from django.db import models

# Create your models here.

first_name = models.CharField(max_length=20)
last_name = models.CharField(max_length=20)
email = models.EmailField(max_length=None)
store = models.CharField(max_length=None)
school = models.CharField(max_length=None)
profile_pic = models.ImageField(width_field=200, height_field=200)


def __str__(self):
    return(first_name)
