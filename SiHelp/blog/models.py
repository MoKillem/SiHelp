from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# user model is alr in db 


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default = "Hey, I am here to help you")
    date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=100) #or use foreign key
    unit = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 25.00)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('ad-detail', kwargs = {'pk': self.pk})
    

class Rate(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    
    


class Subject(models.Model):
    code = models.CharField(max_length=100)

