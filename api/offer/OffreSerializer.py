from rest_framework import serializers
from .models import Offre
class OffreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Offre
    fields = (
      'id',
      'title',
      'description',
      'price',
      'start_date',
      'end_date',
      'is_active',
      'destination',
      "image",# Include the destination field
    )
