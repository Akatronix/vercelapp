from django.db import models

# Create your models here.

class SensorData(models.Model): 
    rate = models.CharField(max_length=100)
    oxygen = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)



