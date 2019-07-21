from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tutor = models.BooleanField(default=False)
    pic = models.ImageField(upload_to = 'profile_pic', default = 'download.png')
    phone = models.CharField(max_length=30, default = "0404040404")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.pic.path)

        if img.height > 200 or img.width > 200:
            output_size  = (200,200)
            img.thumbnail(output_size)
            img.save(self.pic.path)