from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Place(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True, editable=True)
    
    

