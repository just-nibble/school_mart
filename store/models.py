from django.db import models

# Create your models here.

from products.models import Product


class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='products/%Y/$m/$d', blank=True)
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
