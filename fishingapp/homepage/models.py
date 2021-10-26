from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
