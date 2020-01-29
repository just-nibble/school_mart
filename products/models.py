from django.db import models

# Create your models here.


class Product(models.Model):
    choice = (('ele', 'electronics'), ('car', 'cars'), ('fsh', 'fashion'), ('sprt', 'sport'), ('home', 'home_appliance'))
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=choice)
