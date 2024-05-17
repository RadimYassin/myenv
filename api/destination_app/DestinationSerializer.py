from rest_framework import serializers
from .models import Destination
from  Event.EventSerializer import EventSerializer
class DestinationSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'