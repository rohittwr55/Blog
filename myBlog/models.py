from django.db import models

# Create your models here.
class Destinations(models.Model):
    img=models.ImageField(upload_to='pics')
    place=models.CharField(max_length=100)
    about=models.CharField(max_length = 100)
    date=models.CharField(max_length = 100, default='SOME STRING')
    description=models.TextField()
    personphoto = models.ImageField(upload_to='pics')
    personName = models.CharField(max_length = 100)
    personDescription = models.TextField()
