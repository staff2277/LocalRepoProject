from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 108)
    description = models.CharField(max_length = 300)
    price = models.IntegerField()
    category = models.CharField(max_length = 200)


    def __str__(self):
        return f"id: {self.name} | description: {self.description} | price: {self.price} | category: {self.category}"

""" 
from cart.models import Product """
""" product1 = Product(name = "iphone 14 pro", description = "The best mobilephone one the planet", price = 450, category = "Electonic Devices") """