from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    rating = models.FloatField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    class Meta:
        ordering = ['-rating']  

    def __str__(self):
        return self.name

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant_images')

    def __str__(self):
        return f"Image for {self.restaurant.name}"
