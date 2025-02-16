from django.db import models

class Engineers(models.Model):
    name = models.CharField(max_length=205)
    relegion = models.CharField(max_length=60)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return f"name: {self.name} | relegion: {self.relegion} | age: {self.age} | salary: {self.salary}"
    

