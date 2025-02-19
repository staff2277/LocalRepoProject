from django.db import models

# Create your models here.
class Afrotours(models.Model):
    country = models.CharField(max_length=108)
    tour_duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"country => {self.country} \n tour_duration => {self.tour_duration} \n price => {self.price} \n"