from django.db import models
from destination_app.models import Destination

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='attractions')
    description = models.TextField()
    image = models.ImageField(upload_to='attraction_images/')

    def __str__(self):
        return self.name
