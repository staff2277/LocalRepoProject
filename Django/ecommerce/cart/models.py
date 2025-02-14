from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 108)
    description = models.CharField(max_length = 300)
    price = models.IntegerField()
    category = models.CharField(max_length = 200)

