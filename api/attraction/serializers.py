# serializers.py
from rest_framework import serializers
from .models import Attraction

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name','destination','description', 'image')
