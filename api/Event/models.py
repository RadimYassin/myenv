from django.db import models
from destination_app.models import Destination
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name