from django.db import models

# Create your models here.

from store.models import Product

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    store = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    profile_pic = models.ImageField(width_field=200, height_field=200)

    def __str__(self):
        return(self.first_name)
