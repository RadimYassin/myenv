from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='destination_images/', null=True, blank=True)

    def __str__(self):
        return self.name
