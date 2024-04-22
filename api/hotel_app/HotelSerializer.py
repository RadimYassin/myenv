from rest_framework import serializers
from .models import Hotel, HotelImage

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ('image',"image_url")

class HotelSerializer(serializers.ModelSerializer):
    images = HotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'location', 'description', 'rating', 'destination', 'images',"pricing")
