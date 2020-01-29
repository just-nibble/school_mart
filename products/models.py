from django.db import models

# Create your models here.
class Product(models.Model):
	type = [electronics, cars, fashion, sports_and_equipment, home_appliances]
	name = models.CharField(max_length=200)
	