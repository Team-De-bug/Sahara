from django.db import models
from django.contrib.auth.models import User
from shop.models import Stock


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='sahara-1.png', upload_to='profile_pics', name="profile_pic")

    def __str__(self):
        return f'{self.user.username} Profile'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.IntegerField(default=0, name="items")
    products = models.ManyToManyField(Stock, blank=True)

    def __str__(self):
        return f'{self.user.username} Cart'
