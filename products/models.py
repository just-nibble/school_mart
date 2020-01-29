from django.db import models

# Create your models here.


class Product(models.Model):
    category = (('ele', 'electronics'), ('car', 'cars'), ('fsh', 'fashion'), ('sprt', 'sport'), ('home', 'home_appliance'))
    name = models.TextField()
    buy = models.CharField(max_length=10, choices=category)
