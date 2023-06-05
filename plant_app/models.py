from django.db import models

# Create your models here.
class Registerdb(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phn=models.IntegerField()
    address=models.TextField()
    password=models.CharField(max_length=10)


class Bookingdb(models.Model):
    pname=models.CharField(max_length=20)
    phone=models.IntegerField()
    address=models.TextField()
    plants=models.CharField(max_length=30)
    





      