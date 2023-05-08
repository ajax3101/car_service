from django.db import models
from .client import Client

class Car(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
