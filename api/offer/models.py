from django.db import models
from django.db import models
from destination_app.models import Destination

class Offre(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    # Add the image field here
    image = models.ImageField(upload_to='offers/')

    def __str__(self):
        return self.title
