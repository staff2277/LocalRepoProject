from django.db import models

class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    
