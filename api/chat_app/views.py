
# Add your generated API key
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from user_app.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
import jwt
# Add your generated API key
from .models import ChatBot

import google.generativeai as genai
genai.configure(api_key="AIzaSyA1J1g0baPidCY8k5HdOHSwbmbh5jLx7Ag")





@api_view(['POST'])
def ask_question(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        if user_id is None:
            raise AuthenticationFailed('Invalid token')

        # Retrieve the user object from the database
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('User does not exist')

        # Your existing code to handle the question
        if request.method == "POST":
            text = request.data.get("text")
            if text is None or text.strip() == "":
                return Response({"error": "Text cannot be empty"}, status=400)
            
            # Check if the text contains keywords related to tourism in Marrakech
            relevant_keywords = [
                "hi", "event in marrakech", "tourism", "visit", "attractions", 
                "places to go", "marrakech", "best place in marrakech", "sights", 
                "activities", "events", "cuisine", "transportation", "culture", 
                "accommodation", "safety"
            ]
            if not any(keyword in text.lower() for keyword in relevant_keywords):
                return Response({"error": "Question must be related to tourism in Marrakech"}, status=400)
            
            # Instantiate the model and generate response
            model = genai.GenerativeModel("gemini-pro")
            chat = model.start_chat()
            response = chat.send_message(text)
            
            # Save the question and response to the database along with user
            chat_entry = ChatBot.objects.create(
                user=user,  # Associate the user with the ChatBot entry
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
        
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
# Add your imports

@api_view(['GET'])
def get_chats(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        if user_id is None:
            raise AuthenticationFailed('Invalid token')

        # Retrieve the user object from the database
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('User does not exist')

        # Retrieve chats for the user from the database
        user_chats = ChatBot.objects.filter(user=user)

        # Serialize the chat data
        chat_data = []
        for chat in user_chats:
            chat_data.append({
                "text_input": chat.text_input,
                "gemini_output": chat.gemini_output,
                "date": chat.date.strftime("%Y-%m-%d %H:%M:%S")
            })

        return Response(chat_data)

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
