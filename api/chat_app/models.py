from django.db import models
from user_app.models import  User


class ChatBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    text_input = models.CharField(max_length=500)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.text_input
