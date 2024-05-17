from rest_framework.decorators import api_view
from rest_framework.response import Response
from user_app.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
import jwt
from .models import ChatBot
import google.generativeai as genai
from datetime import datetime

genai.configure(api_key="AIzaSyA1J1g0baPidCY8k5HdOHSwbmbh5jLx7Ag")

def decode_jwt(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload.get('id')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    except jwt.DecodeError:
        raise AuthenticationFailed('Invalid token!')

def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        raise AuthenticationFailed('User does not exist')

@api_view(['POST'])
def ask_question(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise AuthenticationFailed('Unauthenticated!')

    token = auth_header.split(' ')[1]
    user_id = decode_jwt(token)
    if not user_id:
        raise AuthenticationFailed('Invalid token')

    user = get_user(user_id)

    if request.method == "POST":
        text = request.data.get("text")
        if not text or text.strip() == "":
            return Response({"error": "Text cannot be empty"}, status=400)

        relevant_keywords = [
            "hi", "event in marrakech", "tourism", "visit", "attractions",
            "places to go", "marrakech", "best place in marrakech", "sights",
            "activities", "events", "cuisine", "transportation", "culture",
            "accommodation", "safety"
        ]
        if not any(keyword in text.lower() for keyword in relevant_keywords):
            return Response({"error": "Question must be related to tourism in Marrakech"}, status=400)

        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(text)

        chat_entry = ChatBot.objects.create(
            user=user,
            text_input=text,
            gemini_output=response.text
        )

        response_data = {
            "text_input": chat_entry.text_input,
            "gemini_output": chat_entry.gemini_output,
            "date": chat_entry.date.strftime("%Y-%m-%d %H:%M:%S")
        }
        return Response(response_data)
    else:
        return Response({"error": "Invalid method"}, status=405)

@api_view(['GET'])
def get_chats(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        raise AuthenticationFailed('Unauthenticated!')

    token = auth_header.split(' ')[1]
    user_id = decode_jwt(token)
    if not user_id:
        raise AuthenticationFailed('Invalid token')

    user = get_user(user_id)

    user_chats = ChatBot.objects.filter(user=user)

    chat_data = [
        {
            "text_input": chat.text_input,
            "gemini_output": chat.gemini_output,
            "date": chat.date.strftime("%Y-%m-%d %H:%M:%S")
        }
        for chat in user_chats
    ]

    return Response(chat_data)
