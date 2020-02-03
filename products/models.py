from django.db import models

# Create your models here.

electronics = (('ph', 'phones'), ('tab', 'tablets'), ('acc', 'accessories'))
vehicles = (('ca', 'cars'), ('cyc', 'motorcycles'))
fashion = (("me", "men's"), ("wo", "women's"))
home_appliance = (('coo', 'cookers'), ('fa', 'fans'))


cat = (('electronics', electronics), ('vehicles', vehicles), ('fashion', fashion), ('home appliance', home_appliance))


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/$m/$d', blank=True)
    catalogue = models.CharField(max_length=10, choices=cat, null=True)

    def __str__(self):
        return self.name
