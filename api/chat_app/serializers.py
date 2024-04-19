from rest_framework import serializers
from .models import ChatBot

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBot
        fields = ['id', 'text_input', 'gemini_output', 'date']
