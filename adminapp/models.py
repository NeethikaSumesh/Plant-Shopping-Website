from django.db import models

# Create your models here.
class Plantdb(models.Model):
    plantname=models.CharField(max_length=20)
    plantimages=models.ImageField(upload_to='image', default='null.jpg')
    
class Addb(models.Model):
    plant_image=models.ImageField(upload_to='image', default="null.jpg")
    plantname=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    