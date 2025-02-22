from django.db import models

# Create your models here.
class Africatour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()