from django.db import models
from destination_app.models import Destination

class Transport(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    mode = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.mode} to {self.destination.name}"
