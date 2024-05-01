from django.db import models
from destination_app.models import Destination

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    pricing = models.DecimalField(max_digits=10,decimal_places=2)

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')

    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotel_images/')
    image_url = models.CharField(max_length=255,default="hdhdh")

    def __str__(self):
        return self.hotel.name + " - " + str(self.id)
