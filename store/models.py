from django.db import models

# Create your models here.


cath = (('elec', 'electronics'), ('veh', 'vehicles'), ('fash', 'fashion'), (
    'home', 'home_appliance'))


class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='products/%Y/$m/$d', blank=True)
    category = models.CharField(max_length=20, choices=cath)
    phone_number = models.IntegerField()

    def __str__(self):
        return (self.name)
