from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identity = models.BooleanField(default=False)
    pic = models.ImageField(upload_to = 'profile_pic', default = 'download.png')

    def __str__(self):
        return f'{self.user.username}  Profile'