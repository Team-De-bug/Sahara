from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='sahara-1.png', upload_to='profile_pics', name="profile_pic")

    def __str__(self):
        return f'{self.user.username} Profile'
