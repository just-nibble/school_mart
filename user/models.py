from django.db import models

# Create your models here.

from store.models import Store


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='user/%Y/$m/$d', blank=True)

    def __str__(self):
        return(self.first_name)
