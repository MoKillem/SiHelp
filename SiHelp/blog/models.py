from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# user model is alr in db 


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=100) #or use foreign key
    unit = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs = {'pk': self.pk})
    

class Rate(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

class Subject(models.Model):
    code = models.CharField(max_length=100)

