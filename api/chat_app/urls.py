# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ask_question/', views.ask_question, name='ask_question'),
    path('get_chat/', views.get_chats, name='get_chats'),

]
